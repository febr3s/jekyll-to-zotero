# One of the scripts I tried before finding the definite one

import re

with open("alejandro-guridi-odo.md", "r") as file:
    content = file.read()

lines = content.split("\n")

result = []

line_break_substituted = False
after_second_delimiter = False
first_line_after_delimiter = True
for line in lines:
    if line == "---" and not after_second_delimiter:
        after_second_delimiter = True
        result.append(line)
    elif after_second_delimiter:
        if first_line_after_delimiter:
            result.append(line)
            first_line_after_delimiter = False
        else:
            result.append(re.sub(r"\r\n|\r|\n", "<br>", line))
            if not line_break_substituted:
                line_break_substituted = True
    else:
        result.append(re.sub(r"\r\n|\r|\n", "<br>", line))

with open("alejandro-guridi-oda.md", "w") as file:
    file.write("\n".join(result))

if line_break_substituted:
    print("Line breaks were substituted in file alejandro-guridi-oda.md")
else:
    print("No line breaks were substituted in file alejandro-guridi-oda.md")
