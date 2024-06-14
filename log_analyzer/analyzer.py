import pandas as pd


class LogAnalyzer:
    def __init__(self, files):
        self.files = files
        self.logs = pd.DataFrame()

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

        converters = {
            "timestamp": float,
            "response_header_size": int,
            "client_ip": str,
            "http_response_code": str,
            "response_size": int,
            "http_request_method": str,
            "url": str,
            "username": str,
            "access_type": str,
            "response_type": str,
        }
        logs_list = []

        for file in self.files:
            logs_df = pd.read_csv(
                file,
                sep=r"\s+",
                names=columns,
                converters=converters,
                header=None,
                usecols=range(10),
            )
            logs_list.append(logs_df)

        self.logs = pd.concat(logs_list, ignore_index=True)

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
        start_time = self.logs["timestamp"].min()
        end_time = self.logs["timestamp"].max()
        duration = end_time - start_time
        return float(len(self.logs) / duration) if duration > 0 else 0

    def total_bytes_exchanged(self):
        return int(
            self.logs["response_size"].sum() + self.logs["response_header_size"].sum()
        )
