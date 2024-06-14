from unittest.mock import Mock

import pytest

from log_analyzer.utils import file_validator


def test_single_file_supported_format():
    args = Mock()
    args.input = ["file1.json"]
    try:
        file_validator(args)
    except ValueError:
        pytest.fail("file_validator raised ValueError unexpectedly!")


def test_single_supported_format_multiple_files():
    args = Mock()
    args.input = ["file1.json", "file2.json", "file3.json"]
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
