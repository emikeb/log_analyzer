import json
from .base_formatter import BaseFormatter


class JsonFormatter(BaseFormatter):

    def format_output(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
        return data
