# Find bare citation keys, e.g. shalev2022ham2pose, and add "@" e.g @shalev2022ham2pose
# Does this by reading the citation keys from references.bib and checking the markdown for matches.
# Written with ChatGPT assistance
# https://chatgpt.com/share/68cde216-5aeb-41e1-a4b2-93e0855f6b98
import re
import sys
from pathlib import Path
import argparse


def extract_citation_keys(bib_file_path):
    citation_keys = []
    with open(bib_file_path, "r") as file:
        for line in file:
            match = re.match(r"@\w+\{([^,]+),", line)
            if match:
                citation_keys.append(match.group(1))
    return citation_keys


def find_bare_citations(markdown_file_path, citation_keys):
    with open(markdown_file_path, "r") as file:
        content = file.readlines()

    # updated_content = []
    issues = []
    in_code_block = False
    in_comment = False

    for i, line in enumerate(content):
        # Check if we are entering or exiting a code block
        if line.strip().startswith("<!--"):
            in_comment = True

        if line.strip().startswith("```"):
            in_code_block = not in_code_block

        if not in_code_block and not in_comment:
            for key in citation_keys:
                pattern = re.compile(r"(?<!@)\b" + re.escape(key) + r"\b")
                if pattern.search(line):
                    issues.append(
                        (i + 1, key)
                    )  # Record the line number and citation key
                    line = pattern.sub("@" + key, line)

        if line.strip().endswith("-->"):
            in_comment = False

        # updated_content.append(line)

    # don't fix, just notify
    # with open(markdown_file_path, "w") as file:
    #     file.writelines(updated_content)

    return issues


if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print(f"Usage: {sys.argv[0]} <bib_file_path> <markdown_file_path>")
    #     sys.exit(1)

    # bib_file_path = sys.argv[1]
    # markdown_file_path = sys.argv[2]

    # python find_bare_citations.py references.bib index.md

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "bib_file_path",
        type=Path
    )

    parser.add_argument(
        "markdown_file_path",
        type=Path
    )


    args = parser.parse_args()

    citation_keys = extract_citation_keys(args.bib_file_path)
    issues = find_bare_citations(args.markdown_file_path, citation_keys)

    if issues:

        for line_num, key in issues:
            print(f"Line {line_num}: has missing '@' in citation key '{key}'")
        sys.exit(1)  # exit with an error

    # print(f"Updated {markdown_file_path} with citation keys from {bib_file_path}.")
