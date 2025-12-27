"""
Configuration Example File

Copy this file to config.py and update with your actual values.
NEVER commit config.py to version control.
"""

# Gmail API Configuration
CLIENT_SECRET_FILE = 'client.json'  # Path to Google OAuth credentials
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

# Email Fetching Parameters
MAX_RESULTS = 500  # Maximum number of emails to fetch
INCLUDE_SPAM_TRASH = True  # Include spam and trash emails
LABEL_IDS = None  # Filter by specific Gmail labels (None for all)
QUERY = None  # Gmail search query (None for all)

# Data Paths
ENRON_DATASET_PATH = '/path/to/enron_mail_20150507/maildir'  # Update with actual path
OUTPUT_DIR = './data/'  # Directory for generated JSON files

# Output Filenames
MESSAGES_FILE = 'messages.json'
USERS_FILE = 'users.json'
THREADS_FILE = 'threads.json'
THREAD_USERS_FILE = 'thread-users.json'
USER_THREADS_FILE = 'user-threads.json'

# Pickle File for Pandas DataFrame
EMAILS_DATAFRAME_PICKLE = 'emailsdf.pkl'
