import pytest

from log_analyzer.formatters.xml_formatter import XmlFormatter


@pytest.fixture
def mock_file_path():
    return "mock_file.xml"


@pytest.fixture
def xml_formatter_instance(mock_file_path):
    return XmlFormatter(mock_file_path)


@pytest.fixture
def sample_data():
    return {
        "most_frequent_ip": "10.105.21.199",
        "least_frequent_ip": "10.105.21.193",
        "events_per_second": 1.0446288698154025,
        "total_bytes_exchanged": 106807,
    }


def test_xml_formatter_format_output(xml_formatter_instance, sample_data):
    formatted_output = xml_formatter_instance.format_output(sample_data)

    assert "<data>" in formatted_output
    assert "</data>" in formatted_output
    assert ("<most_frequent_ip>10.105.21.199"
            "</most_frequent_ip>") in formatted_output
    assert ("<least_frequent_ip>10.105.21.193"
            "</least_frequent_ip>") in formatted_output
    assert ("<events_per_second>1.0446288698154025"
            "</events_per_second>") in formatted_output
    assert ("<total_bytes_exchanged>106807"
            "</total_bytes_exchanged>") in formatted_output
