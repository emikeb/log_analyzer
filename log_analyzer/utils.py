import json


def save_results_to_json(results, output_file):
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)
