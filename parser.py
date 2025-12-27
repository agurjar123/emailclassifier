"""
Email Parser Module

This module provides functionality to parse email files and directories,
extracting metadata and content, and organizing them by users and threads.
"""

import re
from os import path, listdir
import sys
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Precompiled regex patterns for performance optimization
time_pattern = re.compile(
    "Date: (?P<data>[A-Z][a-z]+\, \d{1,2} [A-Z][a-z]+ \d{4} \d{2}\:\d{2}\:\d{2} \-\d{4} \([A-Z]{3}\))")
subject_pattern = re.compile("Subject: (?P<data>.*)")
sender_pattern = re.compile("From: (?P<data>.*)")
recipient_pattern = re.compile("To: (?P<data>.*)")
cc_pattern = re.compile("cc: (?P<data>.*)")
bcc_pattern = re.compile("bcc: (?P<data>.*)")
msg_start_pattern = re.compile("\n\n", re.MULTILINE)
msg_end_pattern = re.compile("\n+.*\n\d+/\d+/\d+ \d+:\d+ [AP]M", re.MULTILINE)

# Global data structures for storing parsed email data
feeds = []  # List of all parsed email messages
users = {}  # Mapping of email addresses to unique user IDs
threads = {}  # Mapping of email subjects to unique thread IDs
thread_users = {}  # Mapping of thread IDs to sets of user IDs involved
user_threads = {}  # Mapping of user IDs to sets of thread IDs they're involved in


def parse_email(pathname, orig=True):
    """
    Recursively parse email files from a directory or single file.

    Extracts email metadata (sender, recipients, subject, timestamp) and message content,
    organizing them into threads and user mappings. Generates JSON output files on completion.

    Args:
        pathname (str): Path to email file or directory containing email files
        orig (bool): Whether this is the original call (used to trigger file writing).
                     Default is True. Set to False for recursive calls.

    Returns:
        None: Results are stored in global data structures and written to JSON files

    Side Effects:
        - Updates global feeds, users, threads, thread_users, and user_threads
        - Creates JSON files: messages.json, users.json, threads.json,
          thread-users.json, user-threads.json (when orig=True)
    """
    if path.isdir(pathname):
        print(pathname)
        emails = []
        for child in listdir(pathname):
            # only parse visible files
            if child[0] != ".":
                parse_email(path.join(pathname, child), False)
    else:
        print("file %s" % pathname)
        with open(pathname) as TextFile:
            text = TextFile.read().replace("\r", "")
            try:
                time = time_pattern.search(text).group("data").replace("\n", "")
                subject = subject_pattern.search(text).group("data").replace("\n", "")

                sender = sender_pattern.search(text).group("data").replace("\n", "")

                recipient = recipient_pattern.search(text).group("data").split(", ")
                cc = cc_pattern.search(text).group("data").split(", ")
                bcc = bcc_pattern.search(text).group("data").split(", ")
                msg_start_iter = msg_start_pattern.search(text).end()
                try:
                    msg_end_iter = msg_end_pattern.search(text).start()
                    message = text[msg_start_iter:msg_end_iter]
                except AttributeError:  # not a reply
                    message = text[msg_start_iter:]
                message = re.sub("[\n\r]", " ", message)
                message = re.sub("  +", " ", message)
            except AttributeError:
                logging.error("Failed to parse %s" % pathname)
                return None
            # get user and thread ids
            sender_id = get_or_allocate_uid(sender)
            recipient_id = [get_or_allocate_uid(u.replace("\n", "")) for u in recipient if u != ""]
            cc_ids = [get_or_allocate_uid(u.replace("\n", "")) for u in cc if u != ""]
            bcc_ids = [get_or_allocate_uid(u.replace("\n", "")) for u in bcc if u != ""]
            thread_id = get_or_allocate_tid(subject)
        if thread_id not in thread_users:
            thread_users[thread_id] = set()
        # maintain list of users involved in thread
        users_involved = []
        users_involved.append(sender_id)
        users_involved.extend(recipient_id)
        users_involved.extend(cc_ids)
        users_involved.extend(bcc_ids)
        thread_users[thread_id] |= set(users_involved)
        # maintain list of threads where user is involved
        for user in set(users_involved):
            if user not in user_threads:
                user_threads[user] = set()
            user_threads[user].add(thread_id)

        entry = {"time": time, "thread": thread_id, "sender": sender_id, "recipient": recipient_id, "cc": cc_ids,
                 "bcc": bcc_ids, "message": message}
        feeds.append(entry)
    if orig:
        try:
            with open('messages.json', 'w') as f:
                json.dump(feeds, f)
            with open('users.json', 'w') as f:
                json.dump(users, f)
            with open('threads.json', 'w') as f:
                json.dump(threads, f)
            with open('thread-users.json', 'w') as f:
                for thread in thread_users:
                    thread_users[thread] = list(thread_users[thread])
                json.dump(thread_users, f)
            with open('user-threads.json', 'w') as f:
                for user in user_threads:
                    user_threads[user] = list(user_threads[user])
                json.dump(user_threads, f)
        except IOError:
            print("Unable to write to output files, aborting")
            exit(1)


def get_or_allocate_uid(name):
    """
    Get or create a unique user ID for an email address.

    Args:
        name (str): Email address or user identifier

    Returns:
        int: Unique integer ID for the user. Returns existing ID if user already
             exists, otherwise creates and returns a new ID.
    """
    if name not in users:
        users[name] = len(users)
    return users[name]


def get_or_allocate_tid(name):
    """
    Get or create a unique thread ID for an email subject line.

    Normalizes subject lines by removing common prefixes (RE:, Re:, FWD:, Fwd:)
    to group related emails into the same thread.

    Args:
        name (str): Email subject line

    Returns:
        int: Unique integer ID for the thread. Returns existing ID if thread
             already exists, otherwise creates and returns a new ID.
    """
    parsed_name = re.sub("(RE|Re|FWD|Fwd): ", "", name)
    if parsed_name not in threads:
        threads[parsed_name] = len(threads)
    return threads[parsed_name]


parse_email(sys.argv[1])
