import log_analyzer.config.constants as c

default_output_format = c.JSON

# Current allowed formats
input_allowed_formats = {c.CSV, c.LOG}
output_allowed_formats = {c.CSV, c.JSON, c.XML}
