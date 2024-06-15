import argparse

from log_analyzer.core import Core


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
    core = Core(parse_arguments())
    core.analyze_input()
    output = core.generate_output(core.get_analysis_results())
    print(output)


if __name__ == "__main__":
    main()



