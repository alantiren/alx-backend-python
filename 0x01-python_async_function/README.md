# Python Async Project

## Overview

This project focuses on asynchronous programming in Python, specifically using the `async` and `await` syntax along with the `asyncio` module. It covers the execution of concurrent coroutines, creating asyncio tasks, and utilizing the `random` module.

## Learning Objectives

By the end of this project, you should be able to:

- Understand async and await syntax
- Execute an async program with asyncio
- Run concurrent coroutines
- Create asyncio tasks
- Use the random module

## Project Structure

The project is organized into several files:

- `0-basic_async_syntax.py`: Implementation of the basic asynchronous coroutine `wait_random`.
- `1-concurrent_coroutines.py`: Implementation of an async routine `wait_n` that executes multiple coroutines concurrently.
- `2-measure_runtime.py`: Function to measure the total execution time for `wait_n` and return the average time per coroutine.
- `3-tasks.py`: Function to create an asyncio task for the `wait_random` coroutine.
- `4-tasks.py`: Function to execute multiple coroutines concurrently using asyncio tasks.

## Usage

To test and run the provided functions, you can use the provided test scripts:

- `0-main.py`: Tests the `wait_random` coroutine.
- `1-main.py`: Tests the `wait_n` async routine.
- `2-main.py`: Measures the total execution time for `wait_n` and calculates the average time per coroutine.
- `3-main.py`: Tests the `task_wait_random` function.
- `4-main.py`: Tests the `task_wait_n` function.

## How to Run

To execute the test scripts, you can use the following command:

```bash
./<test_script_name>.py
```

Ensure that you have the required Python version (3.7) and dependencies installed.

## Contributors

- [alan tiren]