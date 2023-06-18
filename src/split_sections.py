import os
import regex as re


def correct_latex_text(text):
    text = text.replace("assets/", "parts/background/assets/")
    text = text.replace(",height=\\textheight", "")  # remoe lineheight from figures
    return text


def find_sections(text):
    return re.findall(r'(\\([sub]*)section\{([\s\S]*?)}(\\label{([\s\S]*?)}\}?)?([\s\S]*?))\\(sub)*section', text,
                      overlapped=True)


def write_section_to_file(output_dir, level, section, label, content, labels, section_prefix="sec:"):
    section = section.replace("\n", " ")
    section_name = label.replace("sec:", "")

    level_num = len(level) // len('sub')
    if level_num >= len(labels):
        labels.append(section_name)
    else:
        labels[level_num] = section_name
    labels = labels[:level_num + 1]  # cut off the rest

    new_label = section_prefix + "-".join(labels).replace("sec:", "")
    f_dir = os.path.join(output_dir, "/".join(labels[:-1]))
    os.makedirs(f_dir, exist_ok=True)
    f_name = os.path.join(f_dir, section_name + ".tex")
    with open(f_name, "w") as f:
        # if len(level) > 0:
        f.write(f"% \\{level}section{{{section}}}\\label{{{new_label}}}\n")
        content = content.replace('\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}', '')
        content_rows = content.splitlines()[:-1]
        f.write("\n".join(content_rows))

    return labels


def split_sections(file_path, output_dir="dst/sections", section_prefix=""):
    os.makedirs(output_dir, exist_ok=True)

    with open(file_path, "r") as f:
        text = f.read()

    text = correct_latex_text(text)
    matches = find_sections(text)
    # print("matches", len(matches))

    abstract = re.search(r'\\begin\{abstract\}([\s\S]*?)\\end\{abstract\}', text)
    if abstract:
        with open(os.path.join(output_dir, "abstract.tex"), "w") as f:
            f.write(abstract.group(1))

    labels = []
    for full_match, level, section, _, label, content, _ in matches:
        if label == "":
            label = section.replace(" ", "-").lower()
        labels = write_section_to_file(output_dir, level, section, label, content, labels, section_prefix)
        # print(f"Written section to {label}.tex")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dir_name = os.path.join(current_dir, "..", "dst", "sections")
    split_sections(os.path.join(current_dir, "..", "dst", "index.tex"), dir_name, section_prefix="")
