# Python Async Comprehension Project

## Overview

This project focuses on asynchronous programming in Python, specifically implementing async generators and comprehensions. The tasks involve creating coroutines, using async comprehensions, and measuring the runtime of parallel comprehensions.

## Project Structure

The project is organized into the following files:

1. **0-async_generator.py**: Contains a coroutine named `async_generator` that loops 10 times, asynchronously waits for 1 second each iteration, and yields a random number between 0 and 10.

2. **1-async_comprehension.py**: Imports `async_generator` from the previous file and defines a coroutine called `async_comprehension` that collects 10 random numbers using async comprehensions over `async_generator`.

3. **2-measure_runtime.py**: Imports `async_comprehension` and implements a `measure_runtime` coroutine that executes `async_comprehension` four times in parallel using `asyncio.gather`. It measures the total runtime and returns the result.

## How to Run

To run the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/alantiren/alx-backend-python.git
   cd alx-backend-python/0x02-python_async_comprehension
   ```

2. Execute the test scripts:

   - Task 0:

     ```bash
     ./0-main.py
     ```

   - Task 1:

     ```bash
     ./1-main.py
     ```

   - Task 2:

     ```bash
     ./2-main.py
     ```

## Requirements

- Python 3.7 or higher
- Tested on Ubuntu 18.04 LTS

## Coding Guidelines

- Use PEP 8 style (checked with pycodestyle version 2.5.x).
- Include documentation for all modules and functions.
- Type-annotate all functions and coroutines.
- Ensure all files end with a newline.

## Learning Objectives

By completing this project, you should be able to:

- Write asynchronous generators and comprehensions.
- Use type annotations for functions and coroutines.
- Understand and implement parallel asynchronous code using `asyncio.gather`.

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#asynchronous-comprehensions)
- [Type-hints for generators](https://www.python.org/dev/peps/pep-0484/#id30)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
