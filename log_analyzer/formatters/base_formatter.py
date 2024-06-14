from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def format_output(self, data):
        raise NotImplementedError("Subclasses should implement parse_logs method.")
