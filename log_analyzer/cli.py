import argparse

from log_analyzer.factories.log_analyzer_factory import LogAnalyzerFactory
from log_analyzer.utils import save_results_to_json
from log_analyzer.utils import file_validator


def parse_arguments():
    # We could also use click package here but used argparse to avoid a
    # new dependency
    parser = argparse.ArgumentParser(description="Log Analyzer Tool")
    parser.add_argument("input", nargs="+", help="Path to input log file(s)")
    parser.add_argument("output", help="Path to output JSON file")
    parser.add_argument("--mfip", action="store_true", help="Most frequent IP")
    parser.add_argument("--lfip", action="store_true",
                        help="Least frequent IP")
    parser.add_argument("--eps", action="store_true", help="Events per second")
    parser.add_argument(
        "--bytes", action="store_true", help="Total amount of bytes exchanged"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    file_format = file_validator(args)
    analyzer = LogAnalyzerFactory.create_log_analyzer(args.input, file_format)
    analyzer.parse_logs()

    results = {}
    if args.mfip:
        results["most_frequent_ip"] = analyzer.most_frequent_ip()
    if args.lfip:
        results["least_frequent_ip"] = analyzer.least_frequent_ip()
    if args.eps:
        results["events_per_second"] = analyzer.events_per_second()
    if args.bytes:
        results["total_bytes_exchanged"] = analyzer.total_bytes_exchanged()

    save_results_to_json(results, args.output)
    print(results)


if __name__ == "__main__":
    main()
