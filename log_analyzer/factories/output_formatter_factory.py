from ..formatters.json_formatter import JsonFormatter
from ..formatters.csv_formatter import CsvFormatter
from ..formatters.xml_formatter import XmlFormatter

from config.constants import FileFormat as Ff


class OutputFormatterFactory:
    @staticmethod
    def create_output_formatter(file_path, format_type):
        if format_type.lower() == Ff.JSON.value:
            return JsonFormatter(file_path)
        elif format_type.lower() == Ff.CSV.value:
            return CsvFormatter(file_path)
        elif format_type.lower() == Ff.XML.value:
            return XmlFormatter(file_path)
        else:
            raise ValueError(f"Unsupported format type: {format_type}")
