import config.constants as c
import logging

default_output_format = c.JSON  # not used if argument -f provided

# logging
log_file_path = "../log_analyzer_tool.log"  # default tool log file path
log_file_logging_level = logging.DEBUG  # log level for the log file

# Current allowed formats
input_allowed_formats = {c.CSV, c.LOG}
output_allowed_formats = {c.CSV, c.JSON, c.XML}
