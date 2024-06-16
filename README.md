# Log Analyzer

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://python.org)
[![Build Status](https://github.com/EUGEMIKE1/log_analyzer/actions/workflows/log_analyzer_ci.yml/badge.svg)](https://github.com/EUGEMIKE1/log_analyzer/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

Log Analyzer is a Python tool designed to parse and analyze log files, extracting useful metrics such as the most and least frequent IP addresses, events per second, and total bytes exchanged.

## Current Features

- **Parse Logs**: Read and process log files.
- **Frequent IP Analysis**: Identify the most and least frequent client IP addresses.
- **Event Rate Calculation**: Calculate the number of events per second.
- **Data Summary**: Sum up total bytes exchanged in the log files.

## Table of Contents

- [Installation](#installation)
- [Command Line Interface](#command-line-interface)
- [Examples](#examples)
- [Tools Logs](#tool-logs)
- [Testing](#testing)
- [Continuous Integration](#continuous-integration)
- [Assumptions](#assumptions)
- [License](#license)

## Installation

### Prerequisites

- Python 3.11
- `pip` package manager

### From Source

1. Clone the repository:

    ```bash
    git clone https://github.com/EUGEMIKE1/log_analyzer.git
    cd log_analyzer
    ```

2. Install the package:

    ```bash
    pip install .
    ```

### Using Docker

1. Build the Docker image:

    ```bash
    docker build -t log-analyzer .
    ```

2. Run the container:

    ```bash
    docker run --rm -v $(pwd)/logs:/logs log-analyzer /logs/access.log /logs/output.json --mfip --lfip --eps --bytes
    ```

## Command Line Interface

To analyze logs from the command line, use the following syntax:

```bash
log-analyzer [OPTIONS] input_files... output_file
```
**Options:**

- `--mfip` : Find the most frequent IP address.
- `--lfip` : Find the least frequent IP address.
- `--eps`  : Calculate events per second.
- `--bytes` : Calculate the total bytes exchanged.
- `-f, --out_format`: Specify the output format. Choices are determined by configuration file.
- `--debug`: Enable debug logging in console
- `--version`: Show program's version number

**Example:**

```bash
log-analyzer --mfip --lfip --eps --bytes logs/access.log output.json
```

## Examples

### Most Frequent IP:

```bash
log-analyzer --mfip logs/access.log output.json
```

### Full Analysis:

To perform a comprehensive analysis of your log file, including calculating the most frequent IP address, least frequent IP address, events per second (EPS), and total bytes exchanged, use the following command:

```bash
log-analyzer --mfip --lfip --eps --bytes logs/access.log output.json
```

## Tool logs

By default, Log Analyzer runs with standard logging levels. To enable debug logs for more detailed output, use the `--debug` flag when running the tool.

Additionally, Log Analyzer logs information to the `log_analyzer_tool.log` file. This log file is useful for troubleshooting and can be especially beneficial when running the tool in different containers or when collecting logs to a centralized log aggregator.

**Example**
````text
Sun, 16 Jun 2024 02:03:48: INFO: {'most_frequent_ip': '10.105.21.199', 'least_frequent_ip': '10.105.21.193', 'events_per_second': 2.04, 'total_bytes_exchanged': 70801}
Sun, 16 Jun 2024 02:08:52: INFO: Starting the program with arguments: ['cli.py', '../logs/example_invaalid_data.log', '../output.json', '--mfip', '--lfip', '--eps', '--bytes']
Sun, 16 Jun 2024 02:08:52: ERROR: File not found: [Errno 2] No such file or directory: '../logs/example_invaalid_data.log'
Traceback (most recent call last):
...continue...
````
## Testing

To run the tests for this project, use the following commands:
   
   ```bash
   pip install pytest
   pytest
   ```

## Continuous Integration

### Docker Image CI

The Docker Image CI workflow ensures the Log Analyzer Docker image is built correctly and passes system tests:

- **Trigger**: Automatically runs on `push` and `pull_request` events.
- **Steps**:
  1. **Checkout code**: Retrieves the latest code from the repository.
  2. **Build the Docker image**: Builds the Log Analyzer Docker image using Dockerfile.
  3. **Add sample log file**: Creates a sample log file for testing purposes.
  4. **Run the Docker container**: Executes the Docker container with specified inputs and options.
  5. **Check output**: Validates the output JSON against expected results to ensure correct functionality passing the system test.

### Log Analyzer CI

The Log Analyzer CI workflow integrates DevSecOps best practices to enhance security, quality, and reliability:

- **Trigger**: Automatically runs on `push` and `pull_request` events.
- **Jobs**:
  - **Linting and Static Analysis**: Ensures code style and identifies potential issues using Flake8, Black, isort, and MyPy.
  - **Security Checks**: Validates code security with checks using Safety and Bandit to detect vulnerabilities and insecure practices.
  - **Testing and Coverage**: Executes unit tests with pytest and measures code coverage using Coverage.py to maintain quality and reliability.

By adhering to DevSecOps best practices in our CI workflows, we prioritize security, code quality, and reliability throughout the development lifecycle of Log Analyzer.
Each workflow runs on an ubuntu environment and results of these workflows can be viewed directly in the GitHub Actions tab.

## Assumptions

The project aims to meet diverse input and output format requirements while ensuring fault tolerance and considering future extensibility. 
Additionally, efforts were made to align with DevSecOps best practices and containerize the application.
However, certain design assumptions were made during development:

- All input files must adhere to the same format when processing multiple input files simultaneously.
- During log parsing, if an invalid record is encountered, attempts are made to parse different values, ignoring erroneous data to ensure robust processing.
- When determining the most or least frequent IP addresses, if multiple IPs have the same frequency, the system will select only one IP as the result.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

   

