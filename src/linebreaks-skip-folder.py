# this is the script I will use

import os
import re

# specify the path of the folder containing the Markdown files
folder_path = "/home/febres/Documents/dev/MOREL 2.0/content/_books"

# Define the regular expression pattern to match line breaks
pattern = re.compile(r"(?<!-)\n(?!-)")

# Loop through all files in the specified folder
for file_name in os.listdir(folder_path):
    # Check if the file is a Markdown file
    if file_name.endswith('.md'):
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Open the file for reading and writing
        with open(file_path, "r+") as f:
            # Read the contents of the file
            markdown_text = f.read()
            
            # Find the positions of the first two "---" separators
            first_separator_pos = markdown_text.find("---")
            second_separator_pos = markdown_text.find("---", first_separator_pos + 1)
            
            if second_separator_pos != -1:
                # Substitute all instances of "\n" with "<br>" after the second "---" and not directly after it
                text_before_separator = markdown_text[:second_separator_pos]
                text_after_separator = markdown_text[second_separator_pos:]
                text_after_separator = re.sub(pattern, "<br>", text_after_separator)
                markdown_text = text_before_separator + text_after_separator
            
            # Write the modified text back to the file
            f.seek(0)
            f.write(markdown_text)
            f.truncate()
        
        print(f"Substitution complete for file {file_name}!")
