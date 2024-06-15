from config import config as conf
from log_analyzer.factories.log_analyzer_factory import LogAnalyzerFactory
from log_analyzer.factories.output_formatter_factory import \
    OutputFormatterFactory
from log_analyzer.utils import file_validator


class Core:
    def __init__(self, args):
        self.analyzer = None
        self.args = args

    def analyze_input(self):
        file_format = file_validator(self.args)
        self.analyzer = LogAnalyzerFactory.create_log_analyzer(
            self.args.input, file_format)
        self.analyzer.parse_logs()

    def get_analysis_results(self):
        options = [
            ("most_frequent_ip", self.args.mfip,
             self.analyzer.most_frequent_ip),
            ("least_frequent_ip", self.args.lfip,
             self.analyzer.least_frequent_ip),
            ("events_per_second", self.args.eps,
             self.analyzer.events_per_second),
            ("total_bytes_exchanged", self.args.bytes,
             self.analyzer.total_bytes_exchanged),
        ]
        results = {key: method() for key, flag, method in options if flag}
        return results

    def generate_output(self, results):
        output_formatter = OutputFormatterFactory.create_output_formatter(
            self.args.output, conf.default_output_format
        )
        output = output_formatter.format_output(results)
        return output
