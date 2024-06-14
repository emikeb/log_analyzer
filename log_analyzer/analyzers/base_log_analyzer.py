from abc import ABC, abstractmethod


class BaseLogAnalyzer(ABC):
    def __init__(self, files):
        self.files = files
        self.logs = None

    @abstractmethod
    def parse_logs(self):
        raise NotImplementedError(
            "Subclasses should implement parse_logs method.")

    @abstractmethod
    def most_frequent_ip(self):
        raise NotImplementedError(
            "Subclasses should implement most_frequent_ip method.")

    @abstractmethod
    def least_frequent_ip(self):
        raise NotImplementedError(
            "Subclasses should implement least_frequent_ip method.")

    @abstractmethod
    def events_per_second(self):
        raise NotImplementedError(
            "Subclasses should implement events_per_second method.")

    @abstractmethod
    def total_bytes_exchanged(self):
        raise NotImplementedError(
            "Subclasses should implement total_bytes_exchanged method.")
