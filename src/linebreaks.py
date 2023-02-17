import re

# specify the path of the markdown file
file_path = "/home/febres/Documents/dev/100DaysOfCode/test-linebreaks/alejandro-guridi-oda.md"

# read the contents of the markdown file
with open(file_path, "r") as f:
    markdown_text = f.read()

# substitute all instances of "\n" with "<br>"
markdown_text = re.sub(r"\n", "<br>", markdown_text)

# write the modified text back to the file
with open(file_path, "w") as f:
    f.write(markdown_text)

print("Substitution complete!")
