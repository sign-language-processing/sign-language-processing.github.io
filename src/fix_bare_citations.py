# Find bare citation keys, e.g. shalev2022ham2pose, and add "@" e.g @shalev2022ham2pose
# Does this by reading the citation keys from references.bib and checking the markdown for matches.
# Written with ChatGPT assistance
# https://chatgpt.com/share/8e6057f1-f654-4d04-8528-652fa0392d49
import re

def extract_citation_keys(bib_file_path):
    citation_keys = []
    with open(bib_file_path, 'r') as file:
        for line in file:
            match = re.match(r'@\w+\{([^,]+),', line)
            if match:
                citation_keys.append(match.group(1))
    return citation_keys

def update_markdown_with_citations(markdown_file_path, citation_keys):
    with open(markdown_file_path, 'r') as file:
        content = file.readlines()
    
    updated_content = []
    issues = []
    in_code_block = False

    for i, line in enumerate(content):
        # Check if we are entering or exiting a code block
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        if not in_code_block:
            for key in citation_keys:
                pattern = re.compile(r'(?<!@)\b' + re.escape(key) + r'\b')
                if pattern.search(line):
                    issues.append((i + 1, key))  # Record the line number and citation key
                    line = pattern.sub('@' + key, line)
        updated_content.append(line)
    
    with open(markdown_file_path, 'w') as file:
        file.writelines(updated_content)
    
    return issues


if __name__ == "__main__":
    # Example usage
    bib_file_path = 'references.bib'
    markdown_file_path = 'index.md'

    citation_keys = extract_citation_keys(bib_file_path)
    issues = update_markdown_with_citations(markdown_file_path, citation_keys)

    for line_num, key in issues:
        print(f"Line {line_num}: added '@' to citation key '{key}'")

    print(f"Updated {markdown_file_path} with citation keys from {bib_file_path}.")
