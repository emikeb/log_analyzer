import argparse
import sys

from config import config as conf
from config import constants as cons
from log_analyzer.core import Core
from log_analyzer.utils import set_logger


def parse_arguments():
    # We could also use click package here but used argparse to avoid a
    # new dependency
    parser = argparse.ArgumentParser(description="Log Analyzer Tool")
    parser.add_argument("input", nargs="+", help="Path to input log file(s)")
    parser.add_argument("output", help="Path to output JSON file")
    parser.add_argument("-m", "--mfip", action="store_true", help="Most frequent IP")
    parser.add_argument("-l", "--lfip", action="store_true",
                        help="Least frequent IP")
    parser.add_argument("-e", "--eps", action="store_true", help="Events per second")
    parser.add_argument(
        "-b", "--bytes", action="store_true", help="Total amount of bytes exchanged"
    )
    parser.add_argument(
        "-f", "--out_format",
        choices=[fmt for fmt in cons.output_allowed_formats],
        default=conf.default_output_format,
        help="Output format of the result. Only accepts {}. Default is '{}'."
        .format(cons.output_allowed_formats, conf.default_output_format)
    )
    parser.add_argument('--version', action='version', version=cons.VERSION)
    return parser.parse_args()


def main():
    logger = set_logger()
    logger.info(f'Starting the program with arguments: {sys.argv}')
    try:
        core = Core(parse_arguments())
        core.analyze_input()
        output = core.generate_output(core.get_analysis_results())
        logger.info(output)
        print(output)
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}", exc_info=True)
        sys.exit(1)
    except ValueError as e:
        logger.error(f"ValueError: {e}", exc_info=True)
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()



