# Find bare citation keys, e.g. shalev2022ham2pose, and add "@" e.g @shalev2022ham2pose
# Does this by reading the citation keys from references.bib and checking the markdown for matches.
# Written with ChatGPT assistance
# https://chatgpt.com/share/68cde216-5aeb-41e1-a4b2-93e0855f6b98
# https://chatgpt.com/share/00b023dc-74b8-4cd1-8b78-eadf39658688
import re
import sys
from pathlib import Path
import argparse
import timeit
import uuid


def extract_citation_keys(bib_file_path):
    citation_keys = []
    with open(bib_file_path, "r") as file:
        for line in file:
            match = re.match(r"@\w+\{([^,]+),", line)
            if match:
                citation_keys.append(match.group(1))
    return citation_keys


def find_bare_citations(markdown_file_path:Path, citation_keys:list)->list:
    
    content = markdown_file_path.read_text()

    # Remove HTML comments. regex from https://stackoverflow.com/a/28208465
    content = re.sub("(<!--.*?-->)", "", content, flags=re.DOTALL)

    # Remove Markdown code blocks, regex from https://stackoverflow.com/a/64116935
    markdown_code_block_pattern = re.compile(r'```[^`]*```', re.DOTALL)

    content = markdown_code_block_pattern.sub('', content)




    issues = []


    for citation_key in citation_keys:

        # magical regex from ChatGPT: captures the whole line that has a bare citation.
        pattern = re.compile(r'^.*(?<!@)(?:' + re.escape(citation_key) + r').*$', re.MULTILINE)

        # Find all matching lines
        matches = pattern.findall(content)

        # Print the matches
        # for match in matches:
        #     print(match)

        if matches:
            issue_tuple = citation_key, matches
            issues.append(issue_tuple)

    return issues

if __name__ == "__main__":

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

    print(f"Bibliography had {len(citation_keys)} citations, checking for bare citations:")

    start_time = timeit.default_timer()
    issues = find_bare_citations(args.markdown_file_path, citation_keys)
    elapsed_time = timeit.default_timer() - start_time

    print(f"Bare-citation check complete after ~{elapsed_time:.2f} seconds")


    if issues:
        print("Found the following lines with bare citations:")
        print()

        for citation_key, matches in issues:
            print(f"Citation key: {citation_key}")

            for match in matches:
                print(f"* {match}")
            print()
        sys.exit(1)  # exit with an error

    
