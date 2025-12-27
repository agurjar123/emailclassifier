# Email Classifier

A machine learning-based email classification system that analyzes email threads, identifies question patterns, and organizes email communications using natural language processing.

## Overview

This project provides tools for parsing, analyzing, and classifying emails from Gmail and email datasets (such as the Enron corpus). It uses NLTK's Naive Bayes classifier to detect questions in emails and maintains relationships between users, threads, and messages.

## Features

- **Gmail Integration**: Connect to Gmail API to fetch and analyze emails
- **Email Parsing**: Extract and parse email metadata (sender, recipient, subject, timestamps)
- **Thread Analysis**: Track and organize email threads and conversations
- **Question Detection**: Identify questions in email content using NLP
- **User-Thread Mapping**: Maintain relationships between users and email threads
- **Data Export**: Generate JSON outputs for users, threads, and relationships

## Project Structure

```
emailclassifier/
├── main.py              # Main email parsing and Gmail integration
├── parser.py            # Core email parsing functionality
├── mlscript.py          # ML-based email classification and question detection
├── Google.py            # Google API authentication service
├── quickstart.py        # Gmail API quickstart example
├── client.json          # Google OAuth credentials (not included)
├── README.md            # This file
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
└── data/                # Generated data files (not tracked)
```

## Prerequisites

- Python 3.7+
- Gmail API credentials (OAuth 2.0)
- NLTK data packages

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/emailclassifier.git
cd emailclassifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download NLTK data

```python
import nltk
nltk.download('nps_chat')
nltk.download('punkt')
```

### 4. Set up Gmail API credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API
4. Create OAuth 2.0 credentials
5. Download the credentials and save as `client.json` in the project root

## Usage

### Parsing Emails from Files

To parse email files from a directory:

```bash
python parser.py /path/to/email/directory
```

This will generate the following JSON files:
- `messages.json` - Parsed email messages
- `users.json` - User ID mappings
- `threads.json` - Thread ID mappings
- `thread-users.json` - Thread-to-users relationships
- `user-threads.json` - User-to-threads relationships

### Fetching from Gmail

Run the main script to fetch emails from your Gmail account:

```bash
python main.py
```

On first run, you'll be prompted to authorize the application through your browser.

### Question Detection

The ML script can classify whether an email contains questions:

```python
from mlscript import is_question

text = "How is the project going?"
if is_question(text):
    print("This email contains a question")
```

## API Components

### parser.py

**Functions:**
- `parse_email(pathname, orig=True)` - Recursively parse emails from files/directories
- `get_or_allocate_uid(name)` - Get or create unique user ID
- `get_or_allocate_tid(name)` - Get or create unique thread ID

### Google.py

**Functions:**
- `Create_Service(client_secret_file, api_name, api_version, *scopes)` - Create authenticated Google API service
- `convert_to_RFC_datetime(year, month, day, hour, minute)` - Convert to RFC datetime format

### mlscript.py

**Functions:**
- `analyze(inputfile, tolist, fromlist, body, id, subject)` - Analyze email file
- `is_question(question)` - Detect if text contains a question using NLP

## Configuration

### Email Fetching Parameters

In `main.py`, you can configure:
- `maxRESULTS` - Maximum number of emails to fetch (default: 500)
- `includeSpamTrash` - Include spam/trash emails (default: True)
- `labelIds` - Filter by specific Gmail labels

## Data Privacy

This project handles email data. Please ensure:
- Never commit `client.json` or credential files
- Keep generated JSON files private
- Follow data protection regulations when handling email content
- Review `.gitignore` to exclude sensitive files

## Dependencies

- `google-auth-oauthlib` - Google OAuth authentication
- `google-auth-httplib2` - Google Auth HTTP library
- `google-api-python-client` - Google API client
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `nltk` - Natural language processing

See `requirements.txt` for complete list with versions.

## Known Issues

- Hardcoded file paths in `mlscript.py` need to be parameterized
- Large JSON files should be stored outside version control
- Error handling could be improved in parsing functions

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Uses the Enron Email Dataset for training/testing
- Built with Google Gmail API
- NLP powered by NLTK

## Support

For issues, questions, or contributions, please open an issue on GitHub.
