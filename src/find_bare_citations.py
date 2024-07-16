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
    content = bib_file_path.read_text()
    citation_keys = re.findall(r"@\w+\{([^,]+),", content)
    return citation_keys

def find_bare_citations(markdown_file_path: Path, citation_keys: list) -> list:
    content = markdown_file_path.read_text()

    # Remove HTML comments. regex from https://stackoverflow.com/a/28208465
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)

    # Remove Markdown code blocks, regex from https://stackoverflow.com/a/64116935
    markdown_code_block_pattern = re.compile(r'```[^`]*```', re.DOTALL)
    content = markdown_code_block_pattern.sub('', content)

    for citation_key in citation_keys:
        # Find all positions of the citation key without the @ symbol
        key_pattern = re.compile(re.escape(citation_key))
        matches = []
        for match in key_pattern.finditer(content):
            start_index = match.start()
            # Check if the citation key is not immediately preceded by an @ symbol
            if '@' not in content[start_index-1:start_index]:
                # if the @ is missing, pull out the whole line and return it. 
                line_start = content.rfind('\n', 0, start_index) + 1
                line_end = content.find('\n', start_index)
                if line_end == -1:
                    line_end = len(content)
                line = content[line_start:line_end]
                matches.append(line)
            
            

        if matches:
            yield citation_key, matches


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

    print(f"Parsing {args.bib_file_path} for citations")
    extract_citations_start = timeit.default_timer()
    citation_keys = extract_citation_keys(args.bib_file_path)
    extract_citations_time = timeit.default_timer() - extract_citations_start
    print(f"Finding citations took {extract_citations_time} seconds")


    print(f"Bibliography had {len(citation_keys)} citations")

    print(f"Beginning bare-citations check: checking {args.markdown_file_path}")

    start_time = timeit.default_timer()
    issues = find_bare_citations(args.markdown_file_path, citation_keys)


    print("Found the following lines with bare citations:")
    print()

    # we cannot simply check "if issues" due to using yield
    issues_exist = False 
    for citation_key, matches in issues:
        print(f"Citation key: {citation_key}: {len(matches)} bare citations")

        for i, match in enumerate(matches):
            print(f"{i}: {match}")

            # iff we've gotten here then issues exist and we should set return value to 1 at the end. 
            issues_exist = True
        print()
    elapsed_time = timeit.default_timer() - start_time
    print(f"Bare-citation check complete after ~{elapsed_time} seconds")
    if issues_exist:
        sys.exit(1)  # exit with an error

    
