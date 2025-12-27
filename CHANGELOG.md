# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive README.md with project overview, features, and setup instructions
- CONTRIBUTING.md with contribution guidelines and development standards
- LICENSE file (MIT License)
- requirements.txt with all project dependencies
- Detailed docstrings for all functions in parser.py and Google.py
- Configuration templates (config.example.py, .env.example)
- setup.py for package installation
- Enhanced .gitignore to exclude credentials, data files, and sensitive information

### Changed
- Improved code documentation across all modules
- Updated project structure for better organization

### Fixed
- Added missing import for logging module in parser.py
- Added missing import for datetime module in Google.py

## [1.0.0] - Initial Release

### Features
- Email parsing from files and directories
- Gmail API integration for fetching emails
- Thread and user relationship tracking
- Question detection using NLTK Naive Bayes classifier
- JSON export of parsed data
- Support for Enron email dataset
