# Contributing to Email Classifier

Thank you for your interest in contributing to Email Classifier! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please:

- Be respectful and constructive in discussions
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/emailclassifier.git
   cd emailclassifier
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/originalowner/emailclassifier.git
   ```
4. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Resolve issues and improve stability
- **Feature additions**: Add new functionality
- **Documentation**: Improve README, docstrings, or add examples
- **Performance improvements**: Optimize existing code
- **Test coverage**: Add or improve unit tests
- **Code refactoring**: Improve code quality and maintainability

### Areas for Improvement

Current areas where contributions would be particularly valuable:

1. **Parameterization**: Remove hardcoded paths in `mlscript.py`
2. **Error Handling**: Improve error handling in parsing functions
3. **Testing**: Add comprehensive unit tests
4. **Performance**: Optimize email parsing for large datasets
5. **Documentation**: Add more code examples and use cases
6. **API**: Create a cleaner API interface for the classifier

## Development Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Download required NLTK data:
   ```python
   import nltk
   nltk.download('nps_chat')
   nltk.download('punkt')
   ```

3. Set up Gmail API credentials (for testing):
   - Follow the instructions in README.md
   - Never commit credentials to the repository

4. Run the parser on test data:
   ```bash
   python parser.py /path/to/test/emails
   ```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Maximum line length: 100 characters
- Use 4 spaces for indentation (no tabs)

### Documentation

- Add docstrings to all functions, classes, and modules
- Use Google-style docstrings format:
  ```python
  def example_function(param1, param2):
      """Brief description of function.

      Args:
          param1 (type): Description of param1
          param2 (type): Description of param2

      Returns:
          type: Description of return value

      Raises:
          ExceptionType: Description of when this exception is raised
      """
      pass
  ```

### Code Quality

- Write clean, readable, and maintainable code
- Avoid code duplication
- Keep functions focused on a single responsibility
- Add comments for complex logic
- Handle errors appropriately (don't use bare `except:`)

### Testing

- Add unit tests for new functionality
- Ensure all tests pass before submitting a PR
- Aim for at least 80% code coverage for new code

## Pull Request Process

1. **Update your fork** with the latest upstream changes:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Make your changes** following the coding standards

3. **Test your changes** thoroughly

4. **Commit your changes** with clear, descriptive messages:
   ```bash
   git commit -m "Add feature: Brief description of change"
   ```

   Commit message guidelines:
   - Use present tense ("Add feature" not "Added feature")
   - First line should be 50 characters or less
   - Add detailed description after a blank line if needed
   - Reference issue numbers when applicable

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub:
   - Provide a clear title and description
   - Reference any related issues
   - Describe the changes and their purpose
   - Include screenshots for UI changes
   - List any breaking changes

7. **Respond to feedback** from reviewers:
   - Address all comments and suggestions
   - Push additional commits if needed
   - Mark conversations as resolved when addressed

8. **Wait for approval** from maintainers before merging

## Reporting Bugs

When reporting bugs, please include:

### Bug Report Template

```markdown
**Describe the bug**
A clear and concise description of the bug.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. With parameters '...'
3. See error

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**Environment:**
- OS: [e.g., Ubuntu 20.04, Windows 10, macOS 12]
- Python version: [e.g., 3.8.5]
- Project version/commit: [e.g., v1.0.0 or commit hash]

**Additional context**
- Error messages or stack traces
- Screenshots if applicable
- Sample data (without sensitive information)
```

## Suggesting Enhancements

We welcome feature suggestions! Please include:

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Any alternative solutions or features you've considered.

**Additional context**
- Use cases for this feature
- Example implementations
- Mockups or diagrams if applicable
```

## Development Guidelines

### Adding New Features

1. Discuss major changes by opening an issue first
2. Ensure the feature aligns with project goals
3. Keep features modular and well-documented
4. Add appropriate tests
5. Update relevant documentation

### Code Review Criteria

Pull requests will be evaluated on:

- **Functionality**: Does it work as intended?
- **Code Quality**: Is it clean, readable, and maintainable?
- **Documentation**: Is it well-documented?
- **Testing**: Are there adequate tests?
- **Compatibility**: Does it maintain backward compatibility?
- **Performance**: Does it introduce performance issues?

## Questions?

If you have questions about contributing:

- Open an issue with the `question` label
- Check existing issues and discussions
- Review the README.md for basic information

## License

By contributing to Email Classifier, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing to Email Classifier!
