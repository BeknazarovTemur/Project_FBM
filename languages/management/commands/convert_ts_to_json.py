import json
import re

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("ts_file_path", type=str)
        parser.add_argument("output_json_file_path", type=str)

    def handle(self, *args, **options):
        ts_file_path = options["ts_file_path"]
        output_json_path = options["output_json_file_path"]
        encoding = "utf-8"

        try:
            # Step 1: Read the TypeScript file with the specified encoding
            with open(ts_file_path, encoding=encoding) as file:
                ts_content = file.read()
        except UnicodeDecodeError:
            print(
                "Error: Unable to decode the file with encoding {}. "
                "Try a different encoding.",
                encoding,
            )
            return None

            # Debugging: Display the original content for inspection
        print(
            "Original TS content:\n", ts_content[:200], "\n"
        )  # Limit to first 200 characters for readability

        # Step 2: Remove TypeScript-specific elements
        # Remove 'export const' or similar declarations
        ts_content = re.sub(r"export\s+const\s+\w+\s*=\s*", "", ts_content)

        # Remove comments (single-line and multi-line)
        ts_content = re.sub(r"//.*", "", ts_content)  # Single-line comments
        ts_content = re.sub(r"/\*[\s\S]*?\*/", "", ts_content)  # Multi-line comments

        # Replace single quotes with double quotes
        ts_content = ts_content.replace("'", '"')

        # Remove semicolons at the end of lines
        ts_content = ts_content.replace(";", "")

        # Add double quotes around keys (for example: uz: -> "uz":)
        ts_content = re.sub(r"(\w+)\s*:", r'"\1":', ts_content)

        # Ensure that there are commas between key-value pairs
        # Add commas after closing braces or quotes if they are followed by another key
        ts_content = re.sub(r'(?<=["}])\s*(?=["\w])', ",", ts_content)

        # Remove trailing commas before closing brackets
        ts_content = re.sub(r",\s*}", "}", ts_content)
        ts_content = re.sub(r",\s*]", "]", ts_content)

        # Debugging: Display the cleaned content for inspection
        print("Cleaned TS content (first 200 chars):\n", ts_content[:200], "\n")

        # Step 3: Convert the cleaned content into a Python dictionary
        try:
            data_dict = json.loads(ts_content)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print(f"Problematic JSON content (first 200 chars):\n{ts_content[:200]}")
            return None

        # Step 4: Optionally write the result to a JSON file
        if output_json_path:
            with open(output_json_path, "w", encoding="utf-8") as json_file:
                json.dump(data_dict, json_file, ensure_ascii=False, indent=4)

        return data_dict
