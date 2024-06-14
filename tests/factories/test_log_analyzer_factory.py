import pytest

from config.constants import FileFormat
from log_analyzer.analyzers.csv_log_analyzer import CSVLogAnalyzer
from log_analyzer.analyzers.excel_log_analyzer import ExcelLogAnalyzer
from log_analyzer.analyzers.json_log_analyzer import JSONLogAnalyzer
from log_analyzer.factories.log_analyzer_factory import LogAnalyzerFactory


@pytest.fixture
def sample_file_path():
    return "dummy_path.csv"


def test_create_log_analyzer_csv(sample_file_path):
    analyzer = LogAnalyzerFactory.create_log_analyzer(
        sample_file_path, FileFormat.CSV.value
    )
    assert isinstance(analyzer, CSVLogAnalyzer)
    assert analyzer.files == sample_file_path


def test_create_log_analyzer_json(sample_file_path):
    analyzer = LogAnalyzerFactory.create_log_analyzer(
        sample_file_path, FileFormat.JSON.value
    )
    assert isinstance(analyzer, JSONLogAnalyzer)
    assert analyzer.files == sample_file_path


def test_create_log_analyzer_xlsx(sample_file_path):
    analyzer = LogAnalyzerFactory.create_log_analyzer(
        sample_file_path, FileFormat.XLSX.value
    )
    assert isinstance(analyzer, ExcelLogAnalyzer)
    assert analyzer.files == sample_file_path


def test_create_log_analyzer_invalid_format(sample_file_path):
    with pytest.raises(ValueError):
        LogAnalyzerFactory.create_log_analyzer(sample_file_path, "invalid_format")
