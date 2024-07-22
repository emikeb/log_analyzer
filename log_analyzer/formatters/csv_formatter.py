from log_analyzer.formatters.base_formatter import BaseFormatter


class CsvFormatter(BaseFormatter):
    def format_output(self, data):
        output = ""
        for key, value in data.items():
            output += f"{key},{value}\n"
        return output
