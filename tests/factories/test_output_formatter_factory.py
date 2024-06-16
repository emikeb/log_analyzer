import pytest

from config import constants as cons
from log_analyzer.factories.output_formatter_factory import \
    OutputFormatterFactory
from log_analyzer.formatters.csv_formatter import CsvFormatter
from log_analyzer.formatters.json_formatter import JsonFormatter
from log_analyzer.formatters.xml_formatter import XmlFormatter


def test_output_formatter_factory_json_formatter():
    file_path = "test.json"
    formatter = OutputFormatterFactory.create_output_formatter(file_path, cons.JSON)
    assert isinstance(formatter, JsonFormatter)
    assert formatter.file_path == file_path


def test_output_formatter_factory_csv_formatter():
    file_path = "test.csv"
    formatter = OutputFormatterFactory.create_output_formatter(file_path, cons.CSV)
    assert isinstance(formatter, CsvFormatter)
    assert formatter.file_path == file_path


def test_output_format_factory_xml_formatter():
    file_path = "test.xml"
    formatter = OutputFormatterFactory.create_output_formatter(file_path, cons.XML)
    assert isinstance(formatter, XmlFormatter)
    assert formatter.file_path == file_path


def test_output_format_factory_invalid_format():
    with pytest.raises(ValueError):
        OutputFormatterFactory.create_output_formatter("test.txt", "txt")
