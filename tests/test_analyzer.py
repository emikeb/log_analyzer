import pytest
import pandas as pd
from unittest.mock import patch
from log_analyzer.analyzer import LogAnalyzer

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'timestamp': [1157689324.156, 1157689325.156, 1157689326.156],
        'response_header_size': [1372, 1372, 1372],
        'client_ip': ['10.105.21.199', '10.105.21.199', '10.105.21.200'],
        'http_response_code': ['TCP_MISS/200', 'TCP_MISS/200', 'TCP_MISS/200'],
        'response_size': [399, 399, 399],
        'http_request_method': ['GET', 'GET', 'GET'],
        'url': ['http://www.google-analytics.com/__utm.gif?'] * 3,
        'username': ['badeyek', 'badeyek', 'badeyek'],
        'access_type': ['DIRECT/66.102.9.147', 'DIRECT/66.102.9.147', 'DIRECT/66.102.9.148'],
        'response_type': ['image/gif', 'image/gif', 'image/gif']
    })

@patch('log_analyzer.analyzer.pd.read_csv')
def test_most_frequent_ip(mock_read_csv, sample_data):
    mock_read_csv.return_value = sample_data

    analyzer = LogAnalyzer(['dummy_path.csv'])
    analyzer.parse_logs()
    assert analyzer.most_frequent_ip() == '10.105.21.199'

@patch('log_analyzer.analyzer.pd.read_csv')
def test_least_frequent_ip(mock_read_csv, sample_data):
    mock_read_csv.return_value = sample_data

    analyzer = LogAnalyzer(['dummy_path.csv'])
    analyzer.parse_logs()
    assert analyzer.least_frequent_ip() == '10.105.21.200'

@patch('log_analyzer.analyzer.pd.read_csv')
def test_events_per_second(mock_read_csv, sample_data):
    mock_read_csv.return_value = sample_data

    analyzer = LogAnalyzer(['dummy_path.csv'])
    analyzer.parse_logs()
    assert analyzer.events_per_second() == 1.5

@patch('log_analyzer.analyzer.pd.read_csv')
def test_total_bytes_exchanged(mock_read_csv, sample_data):
    mock_read_csv.return_value = sample_data

    analyzer = LogAnalyzer(['dummy_path.csv'])
    analyzer.parse_logs()
    assert analyzer.total_bytes_exchanged() == 5313

@patch('log_analyzer.analyzer.pd.read_csv')
def test_empty_file(mock_read_csv):
    empty_data = pd.DataFrame(columns=[
        'timestamp', 'response_header_size', 'client_ip', 'http_response_code',
        'response_size', 'http_request_method', 'url', 'username', 'access_type', 'response_type'
    ])
    mock_read_csv.return_value = empty_data

    analyzer = LogAnalyzer(['dummy_path.csv'])
    analyzer.parse_logs()
    assert analyzer.most_frequent_ip() is None
    assert analyzer.least_frequent_ip() is None
    assert analyzer.events_per_second() == 0.0
    assert analyzer.total_bytes_exchanged() == 0

@patch('log_analyzer.analyzer.pd.read_csv')
def test_single_entry(mock_read_csv, sample_data):
    single_entry_data = sample_data.iloc[:1]
    mock_read_csv.return_value = single_entry_data

    analyzer = LogAnalyzer(['dummy_path.csv'])
    analyzer.parse_logs()
    assert analyzer.most_frequent_ip() == '10.105.21.199'
    assert analyzer.least_frequent_ip() == '10.105.21.199'
    assert analyzer.events_per_second() == 0.0
    assert analyzer.total_bytes_exchanged() == 399 + 1372
