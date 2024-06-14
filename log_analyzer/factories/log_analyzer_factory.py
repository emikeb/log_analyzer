from ..analyzers.json_log_analyzer import JSONLogAnalyzer
from ..analyzers.csv_log_analyzer import CSVLogAnalyzer
from ..analyzers.excel_log_analyzer import ExcelLogAnalyzer

from config.constants import FileFormat


class LogAnalyzerFactory:
    @staticmethod
    def create_log_analyzer(file_path, file_format):
        if file_format == FileFormat.LOG:
            return CSVLogAnalyzer(file_path)
        if file_format == FileFormat.CSV.value:
            return CSVLogAnalyzer(file_path)
        elif file_format == FileFormat.JSON.value:
            return JSONLogAnalyzer(file_path)
        elif file_format == FileFormat.XLSX.value:
            return ExcelLogAnalyzer(file_path)
        else:
            raise ValueError("Unsupported file format {}.".format(file_format))
