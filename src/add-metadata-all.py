# Use this when all the files you want to modify are on the same folder

import os

# Directory containing the .md files
directory = "path/to/directory"

# Loop through all the files in the directory
for filename in os.listdir(directory):
    # Only process .md files
    if filename.endswith(".md"):
        file_path = os.path.join(directory, filename)
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        # Check if the "periodo:" line is present in the file. 
        # Replace periodo with the one that is right before the metadata container that you want to add and/or modify in bulk
        periodo_line = None
        for i, line in enumerate(lines):
            if line.strip() == "periodo:":
                periodo_line = i
                break
        
        # If the "periodo:" line was found, insert the "featured: false" line right after it
        # Replace "featured" with the metadata container that you want to add and/or modify in bulk

        if periodo_line is not None:
            lines.insert(periodo_line + 1, "featured: false\n")
        
        # Write the updated file content
        with open(file_path, "w") as file:
            file.writelines(lines)
