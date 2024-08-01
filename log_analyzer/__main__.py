import sys

from log_analyzer.cli import parse_arguments
from log_analyzer.core import Core
from log_analyzer.utils import set_logger


def main():
    args = parse_arguments()
    logger = set_logger(console_debug=args.debug)
    logger.info(f"Starting the program with arguments: {sys.argv}")
    try:
        core = Core(args)
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


if __name__ == "__main__":
    main()
