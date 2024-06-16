import pandas as pd
import numpy as np

from .base_log_analyzer import BaseLogAnalyzer


def parse_timestamp(value):
    try:
        return float(value)
    except ValueError:
        return 0.0


def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return 0


class CSVLogAnalyzer(BaseLogAnalyzer):
    def parse_logs(self):
        columns = [
            "timestamp",
            "response_header_size",
            "client_ip",
            "http_response_code",
            "response_size",
            "http_request_method",
            "url",
            "username",
            "access_type",
            "response_type",
        ]

        logs_list = []

        for file in self.files:
            logs_df = pd.read_csv(
                file,
                sep=r"\s+",
                names=columns,
                header=None,
                usecols=range(10),
                dtype=str
            )
            logs_list.append(logs_df)

        self.logs = pd.concat(logs_list, ignore_index=True)

        self.logs["timestamp"] = self.logs["timestamp"].apply(
            parse_timestamp)
        self.logs["response_header_size"] = self.logs[
            "response_header_size"].apply(parse_int)
        self.logs["response_size"] = self.logs["response_size"].apply(
            parse_int)

    def most_frequent_ip(self):
        if self.logs.empty:
            return None
        return self.logs["client_ip"].value_counts().idxmax()

    def least_frequent_ip(self):
        if self.logs.empty:
            return None
        return self.logs["client_ip"].value_counts().idxmin()

    def events_per_second(self):
        if self.logs.empty:
            return 0

        valid_start_timestamps = self.logs["timestamp"][
            self.logs["timestamp"] > 0]
        valid_end_timestamps = self.logs["timestamp"][
            self.logs["timestamp"] > 0]

        start_time = valid_start_timestamps.min() if not valid_start_timestamps.empty else 0
        end_time = valid_end_timestamps.max() if not valid_end_timestamps.empty else 0
        duration = end_time - start_time
        return float(len(self.logs) / duration) if duration > 0 else 0

    def total_bytes_exchanged(self):
        return int(
            self.logs["response_size"].sum() + self.logs[
                "response_header_size"].sum()
        )
