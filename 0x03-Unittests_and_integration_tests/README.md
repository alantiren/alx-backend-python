# 0x03-Unittests_and_Integration_Tests

## Introduction

This project focuses on implementing unit tests and integration tests for a Python codebase. It covers testing various functions and methods using different testing techniques, such as parameterization, mocking HTTP calls, and testing memoization.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [How to Run Tests](#how-to-run-tests)
- [Contributing](#contributing)

## Learning Objectives

By the end of this project, you should be able to:

- Understand the difference between unit tests and integration tests.
- Apply common testing patterns such as mocking, parametrizations, and fixtures.
- Write unit tests and integration tests for Python code.
- Use the `unittest` framework and related libraries for testing.

## Requirements

- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Follow the specified coding style using pycodestyle (version 2.5).
- Include necessary documentation for modules, classes, and functions.
- Ensure all functions and coroutines are type-annotated.

## Project Structure

The project consists of the following files:

- `utils.py`: Contains generic utilities for a GitHub organization client.
- `client.py`: Implements a GitHub organization client using the utilities from `utils.py`.
- `fixtures.py`: Provides fixtures for integration tests.
- `test_utils.py`: Unit tests for functions in `utils.py`.
- `test_client.py`: Unit tests and integration tests for the `GithubOrgClient` class.

## How to Run Tests

Execute the tests using the following command:

```bash
$ python -m unittest discover
```

Make sure to meet the requirements mentioned in the project specifications.

## Contributing

If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.
