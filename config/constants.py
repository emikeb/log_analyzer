from enum import Enum


class FileFormat(Enum):
    JSON = ".json"
    XLSX = ".xlsx"
    CSV = ".csv"
    LOG = ".log"
    XML = ".xml"


allowed_formats = {format_.value for format_ in FileFormat}
