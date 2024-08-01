import json
from unittest.mock import Mock, patch

import pytest

from log_analyzer.utils import file_validator
from log_analyzer.utils import set_logger_config, init_logging


def test_single_file_supported_format():
    args = Mock()
    args.input = ["file1.log"]
    try:
        file_validator(args)
    except ValueError:
        pytest.fail("file_validator raised ValueError unexpectedly!")


def test_single_supported_format_multiple_files():
    args = Mock()
    args.input = ["file1.csv", "file2.csv", "file3.csv"]
    try:
        file_validator(args)
    except ValueError:
        pytest.fail("file_validator raised ValueError unexpectedly!")


def test_multiple_formats():
    args = Mock()
    args.input = ["file1.json", "file2.csv", "file3.json"]
    with pytest.raises(ValueError, match="Not all files have the same format"):
        file_validator(args)


def test_unsupported_format():
    args = Mock()
    args.input = ["file1.unsupported"]
    with pytest.raises(ValueError, match="Unsupported file format"):
        file_validator(args)


def test_logging_with_default_config(monkeypatch):
    monkeypatch.setenv("ANALYZER_LOGGING_CONFIG", "")
    with patch("log_analyzer.utils.logging.config") as mock:
        init_logging()
        mock.dictConfig.assert_called_once_with(set_logger_config())


def test_logging_with_custom_config(tmp_path, monkeypatch):
    config = {"version": 1}
    config_file = tmp_path / "log_analyzer.json"
    config_file.write_text(json.dumps(config))
    monkeypatch.setenv("ANALYZER_LOGGING_CONFIG", str(config_file))
    init_logging()
    with patch("log_analyzer.utils.logging.config") as mock:
        init_logging()
        mock.dictConfig.assert_called_once_with(config)
