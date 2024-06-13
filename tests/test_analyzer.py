import unittest
import pandas as pd
from log_analyzer.analyzer import LogAnalyzer
from unittest.mock import patch


class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
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
    def test_most_frequent_ip(self, mock_read_csv):
        mock_read_csv.return_value = self.sample_data

        analyzer = LogAnalyzer(['dummy_path.csv'])
        analyzer.parse_logs()
        self.assertEqual(analyzer.most_frequent_ip(), '10.105.21.199')

    @patch('log_analyzer.analyzer.pd.read_csv')
    def test_least_frequent_ip(self, mock_read_csv):
        mock_read_csv.return_value = self.sample_data

        analyzer = LogAnalyzer(['dummy_path.csv'])
        analyzer.parse_logs()
        self.assertEqual(analyzer.least_frequent_ip(), '10.105.21.200')

    @patch('log_analyzer.analyzer.pd.read_csv')
    def test_events_per_second(self, mock_read_csv):
        mock_read_csv.return_value = self.sample_data

        analyzer = LogAnalyzer(['dummy_path.csv'])
        analyzer.parse_logs()
        self.assertEqual(analyzer.events_per_second(), 1.5)

    @patch('log_analyzer.analyzer.pd.read_csv')
    def test_total_bytes_exchanged(self, mock_read_csv):
        mock_read_csv.return_value = self.sample_data

        analyzer = LogAnalyzer(['dummy_path.csv'])
        analyzer.parse_logs()
        self.assertEqual(analyzer.total_bytes_exchanged(), 5313)

    @patch('log_analyzer.analyzer.pd.read_csv')
    def test_empty_file(self, mock_read_csv):
        empty_data = pd.DataFrame(columns=self.sample_data.columns)
        mock_read_csv.return_value = empty_data

        analyzer = LogAnalyzer(['dummy_path.csv'])
        analyzer.parse_logs()
        self.assertEqual(analyzer.most_frequent_ip(), None)
        self.assertEqual(analyzer.least_frequent_ip(), None)
        self.assertEqual(analyzer.events_per_second(), 0.0)
        self.assertEqual(analyzer.total_bytes_exchanged(), 0)

    @patch('log_analyzer.analyzer.pd.read_csv')
    def test_single_entry(self, mock_read_csv):
        single_entry_data = self.sample_data.iloc[:1]
        mock_read_csv.return_value = single_entry_data

        analyzer = LogAnalyzer(['dummy_path.csv'])
        analyzer.parse_logs()
        self.assertEqual(analyzer.most_frequent_ip(), '10.105.21.199')
        self.assertEqual(analyzer.least_frequent_ip(), '10.105.21.199')
        self.assertEqual(analyzer.events_per_second(), 0.0)
        self.assertEqual(analyzer.total_bytes_exchanged(), 399 + 1372)


if __name__ == '__main__':
    unittest.main()
