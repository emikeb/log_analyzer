import argparse

from log_analyzer.config import config as conf
from log_analyzer.config import constants as cons


def parse_arguments():
    parser = argparse.ArgumentParser(description="Log Analyzer Tool")
    parser.add_argument("input", nargs="+", help="Path to input log file(s)")
    parser.add_argument("output", help="Path to output JSON file")
    parser.add_argument("-m", "--mfip", action="store_true",
                        help="Most frequent IP")
    parser.add_argument("-l", "--lfip", action="store_true",
                        help="Least frequent IP")
    parser.add_argument("-e", "--eps", action="store_true",
                        help="Events per second")
    parser.add_argument("-b", "--bytes", action="store_true",
                        help="Total amount of bytes exchanged")
    parser.add_argument(
        "-f",
        "--out_format",
        choices=[fmt for fmt in conf.output_allowed_formats],
        default=conf.default_output_format,
        help=("Output format of the result."
              " Only accepts {}. Default is '{}'.").format(
            conf.output_allowed_formats, conf.default_output_format),
    )
    parser.add_argument(
        "--debug", action="store_true", help="Enable debug logging in console"
    )
    parser.add_argument("--version", action="version", version=cons.VERSION)
    return parser.parse_args()
