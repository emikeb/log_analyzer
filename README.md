# Log Analyzer

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://python.org)
[![Build Status](https://github.com/EUGEMIKE1/log_analyzer/actions/workflows/log_analyzer_ci.yml/badge.svg)](https://github.com/EUGEMIKE1/log_analyzer/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

Log Analyzer is a Python tool designed to parse and analyze log files, extracting useful metrics such as the most and least frequent IP addresses, events per second, and total bytes exchanged.

## Features

- **Parse Logs**: Efficiently read and process log files.
- **Frequent IP Analysis**: Identify the most and least frequent client IP addresses.
- **Event Rate Calculation**: Calculate the number of events per second.
- **Data Summary**: Sum up total bytes exchanged in the log files.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Command Line Interface](#command-line-interface)
  - [Python API](#python-api)
- [Examples](#examples)
- [Testing](#testing)
- [Contributing](#contributing)
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

## Usage

### Command Line Interface

To analyze logs from the command line, use the following syntax:

```bash
log-analyzer [OPTIONS] input_files... output_file
```
**Options:**

- `--mfip` : Find the most frequent IP address.
- `--lfip` : Find the least frequent IP address.
- `--eps`  : Calculate events per second.
- `--bytes` : Calculate the total bytes exchanged.

**Example:**

```bash
log-analyzer --mfip --lfip --eps --bytes logs/access.log output.json
```
### Python API

You can also use the log analyzer as a Python module:

```python
from log_analyzer.analyzer import LogAnalyzer

files = ['path/to/access.log']
analyzer = LogAnalyzer(files)
analyzer.parse_logs()

print(analyzer.most_frequent_ip())
print(analyzer.least_frequent_ip())
print(analyzer.events_per_second())
print(analyzer.total_bytes_exchanged())
```
## Examples

### Most Frequent IP:

```bash
log-analyzer --mfip logs/access.log output.json
```

### Full Analysis

To perform a comprehensive analysis of your log file, including calculating the most frequent IP address, least frequent IP address, events per second (EPS), and total bytes exchanged, use the following command:

```bash
log-analyzer --mfip --lfip --eps --bytes logs/access.log output.json
```

## Testing

To run the tests for this project, follow these steps:

1. **Install pytest**: If you haven't installed pytest yet, you can do so using pip:
   
   ```bash
   pip install pytest
   pytest
   ```
## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

   

