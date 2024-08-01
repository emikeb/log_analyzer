import sys
import logging

from log_analyzer.cli import parse_arguments
from log_analyzer.core import Core
from log_analyzer.utils import set_logger_config

logger = logging.getLogger(__name__)

def main():
    args = parse_arguments()
    set_logger_config(console_debug=args.debug)

    logger.info(f"Starting the program with arguments: {sys.argv}")
    try:
        core = Core(args)
        core.analyze_input()
        output = core.generate_output(core.get_analysis_results())
        logger.info(output)
        print(output)
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}", exc_info=False)
        sys.exit(1)
    except ValueError as e:
        logger.error(f"ValueError: {e}", exc_info=False)
        sys.exit(1)


if __name__ == "__main__":
    main()
