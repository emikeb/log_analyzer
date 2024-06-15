import json
from pathlib import Path

from config import constants as cons


def file_validator(args):
    file_formats = {Path(file_path).suffix for file_path in args.input}
    if len(file_formats) != 1:
        raise ValueError(
            "Not all files have the same format: {}".format(", ".join(file_formats))
        )
    file_format = file_formats.pop()
    if file_format not in cons.allowed_formats:
        raise ValueError("Unsupported file format {}.".format(format))
    return file_format
