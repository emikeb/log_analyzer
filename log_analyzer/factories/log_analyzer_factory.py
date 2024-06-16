from config import constants as cons

from ..analyzers.csv_log_analyzer import CSVLogAnalyzer
from ..analyzers.excel_log_analyzer import ExcelLogAnalyzer
from ..analyzers.json_log_analyzer import JSONLogAnalyzer


class LogAnalyzerFactory:
    @staticmethod
    def create_log_analyzer(file_path, file_format):
        if file_format == cons.LOG:
            return CSVLogAnalyzer(file_path)
        if file_format == cons.CSV:
            return CSVLogAnalyzer(file_path)
        elif file_format == cons.JSON:
            return JSONLogAnalyzer(file_path)
        elif file_format == cons.XLSX:
            return ExcelLogAnalyzer(file_path)
        else:
            raise ValueError("Unsupported file format {}.".format(file_format))
