import os
import regex as re

with open("dst/index.tex", "r") as f:
    text = f.read()

# Correct assets path
text = text.replace("assets/", "parts/background/assets/")
# Remove lineheight
text = text.replace(",height=\\textheight", "")

matches = re.findall(r'(\\([sub]*)section\{([\s\S]*?)}\\label{([\s\S]*?)}\}([\s\S]*?))\\(sub)*section', text,
                     overlapped=True)
print("matches", len(matches))

dir_name = "dst/sections"
os.makedirs(dir_name, exist_ok=True)

labels = []
last_level = ""

for full_match, level, section, label, content, _ in matches:
    section = section.replace("\n", " ")

    level_num = len(level) // len('sub')
    if level_num >= len(labels):
        labels.append(label)
    else:
        labels[level_num] = label
    labels = labels[:level_num + 1]  # cut off the rest

    new_label = "-".join(labels)
    f_dir = os.path.join(dir_name, "/".join(labels[:-1]))
    os.makedirs(f_dir, exist_ok=True)
    f_name = os.path.join(f_dir, label + ".tex")
    with open(f_name, "w") as f:
        if len(level) > 0:
            f.write(f"% \\{level}section{{{section}}}\\label{{{new_label}}}\n")
        content_rows = content.splitlines()[:-1]
        f.write("\n".join(content_rows))

    print(f_name)
