import logging
import sys
from pathlib import Path

from config import config as conf


def file_validator(args):
    file_formats = {Path(file_path).suffix for file_path in args.input}
    if len(file_formats) != 1:
        raise ValueError(
            "Not all files have the same format: {}".format(
                ", ".join(file_formats))
        )
    file_format = file_formats.pop()
    if file_format not in conf.input_allowed_formats:
        raise ValueError("Unsupported file format {}.".format(format))
    return file_format


def set_logger(name="logger", log_file=conf.log_file_path,
               console_debug=False):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)

        # logging to the file
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            "%(asctime)s: %(levelname)s: %(message)s",
            datefmt="%a, %d %b %Y %H:%M:%S"
        )
        fh.setFormatter(file_formatter)

        # logging to the console
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(logging.DEBUG if console_debug else logging.WARNING)
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        sh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger
