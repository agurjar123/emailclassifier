"""
Google API Service Module

Provides authentication and service creation utilities for Google APIs,
including Gmail API integration with OAuth 2.0 authentication.
"""

import pickle
import os
import datetime
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    """
    Create an authenticated Google API service instance.

    Handles OAuth 2.0 authentication flow, token storage, and automatic token refresh.
    Stores tokens in pickled files for reuse across sessions.

    Args:
        client_secret_file (str): Path to the client secret JSON file from Google Cloud Console
        api_name (str): Name of the Google API (e.g., 'gmail', 'drive')
        api_version (str): Version of the API (e.g., 'v1')
        *scopes: Variable length argument list of OAuth scopes required

    Returns:
        Resource: An authenticated Google API service object, or None if creation fails

    Side Effects:
        - Creates 'token files' directory if it doesn't exist
        - Stores authentication tokens as pickle files
        - Opens browser for OAuth authorization on first run or token expiry

    Example:
        >>> service = Create_Service('client.json', 'gmail', 'v1',
        ...                          ['https://mail.google.com/'])
        >>> if service:
        ...     print('Gmail service created successfully')
    """
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None
    working_dir = os.getcwd()
    token_dir = 'token files'

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    ### Check if token dir exists first, if not, create the folder
    if not os.path.exists(os.path.join(working_dir, token_dir)):
        os.mkdir(os.path.join(working_dir, token_dir))

    if os.path.exists(os.path.join(working_dir, token_dir, pickle_file)):
        with open(os.path.join(working_dir, token_dir, pickle_file), 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(os.path.join(working_dir, token_dir, pickle_file), 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print(e)
        print(f'Failed to create service instance for {API_SERVICE_NAME}')
        os.remove(os.path.join(working_dir, token_dir, pickle_file))
        return None


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    """
    Convert date and time components to RFC 3339 datetime format.

    Args:
        year (int): Year (default: 1900)
        month (int): Month (1-12) (default: 1)
        day (int): Day of month (1-31) (default: 1)
        hour (int): Hour (0-23) (default: 0)
        minute (int): Minute (0-59) (default: 0)

    Returns:
        str: ISO 8601 formatted datetime string with 'Z' timezone indicator

    Example:
        >>> convert_to_RFC_datetime(2023, 12, 25, 15, 30)
        '2023-12-25T15:30:00Z'
    """
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt