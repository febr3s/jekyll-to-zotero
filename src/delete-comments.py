import os
import re

# Define the directory to traverse
directory = '/home/febres/Documents/dev/100DaysOfCode/0-Ch_1-_Orinales_fuera_de_sus_casillas'

# Define the regular expression to match "<< >>" and everything between them
pattern = r"<<.*?>>"

# Traverse through the directory and its subdirectories
for subdir, dirs, files in os.walk(directory):
    for file in files:
        # Check if the file is a Markdown file
        if file.endswith('.md'):
            # Read the contents of the file
            filepath = os.path.join(subdir, file)
            with open(filepath, 'r') as f:
                contents = f.read()
            
            # Remove "<< >>" and everything between them
            new_contents = re.sub(pattern, '', contents)
            
            # Write the new contents to the file
            with open(filepath, 'w') as f:
                f.write(new_contents)