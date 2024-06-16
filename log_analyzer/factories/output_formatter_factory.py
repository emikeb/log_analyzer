from config import constants as cons

from ..formatters.csv_formatter import CsvFormatter
from ..formatters.json_formatter import JsonFormatter
from ..formatters.xml_formatter import XmlFormatter


class OutputFormatterFactory:
    @staticmethod
    def create_output_formatter(file_path, format_type):
        if format_type.lower() == cons.JSON:
            return JsonFormatter(file_path)
        elif format_type.lower() == cons.CSV:
            return CsvFormatter(file_path)
        elif format_type.lower() == cons.XML:
            return XmlFormatter(file_path)
        else:
            raise ValueError(f"Unsupported format type: {format_type}")
