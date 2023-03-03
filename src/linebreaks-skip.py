# One of the scripts I tried before finding the definite one

import re

# specify the path of the markdown file
file_path = "/home/febres/Documents/dev/100DaysOfCode/test-linebreaks/algunos-versos-alejandro-arango.md"

# read the contents of the markdown file
with open(file_path, "r") as f:
    markdown_text = f.read()

# find the positions of the first two "---" separators
first_separator_pos = markdown_text.find("---")
second_separator_pos = markdown_text.find("---", first_separator_pos + 1)

if second_separator_pos != -1:
    # substitute all instances of "\n" with "<br>" after the second "---" and not directly after it
    text_before_separator = markdown_text[:second_separator_pos]
    text_after_separator = markdown_text[second_separator_pos:]
    text_after_separator = re.sub(r"(?<!-)\n(?!-)", "<br>", text_after_separator)
    markdown_text = text_before_separator + text_after_separator

# write the modified text back to the file
with open(file_path, "w") as f:
    f.write(markdown_text)

print("Substitution complete!")
