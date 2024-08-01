
import json
import logging.config
import os

from pathlib import Path

from log_analyzer.config import config as conf


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



def set_logger_config(log_file="log_analyzer_tool.log", console_debug=False):
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "bare": {
                "format": "[%(asctime)s] [%(process)d] [%(levelname)s] %(name)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "file": {
                "format": "%(asctime)s: %(levelname)s: %(message)s",
                "datefmt": "%a, %d %b %Y %H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "formatter": "bare",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "level": "DEBUG" if console_debug else "WARNING",
            },
            "file": {
                "formatter": "file",
                "class": "logging.FileHandler",
                "filename": log_file,
                "level": "DEBUG",
            },
        },
        "loggers": {
            "": {
                "handlers": ["console", "file"],
                "level": "DEBUG",
            },
        },
    }

    return config

def init_logging():
    config = set_logger_config()

    path = os.getenv("ANALYZER_LOGGING_CONFIG")
    if path:
        with open(path, encoding="utf-8") as f:
            config = json.load(f)

    logging.config.dictConfig(config)
