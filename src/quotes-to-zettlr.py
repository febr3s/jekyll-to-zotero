import os
import csv

# Set the directory to search for Markdown files in
directory = "/home/febres/Documents/dev/100DaysOfCode/0-Ch_1-_Orinales_fuera_de_sus_casillas"

# Set the name of the CSV file containing the replacements
csv_file = "/home/febres/Documents/dev/100DaysOfCode/list-quotes.csv"

# Read the replacements from the CSV file
replacements = {}
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        replacements[row[0]] = row[1]

# Loop through all Markdown files in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                contents = f.read()

            # Replace the strings in the file contents
            for old_string, new_string in replacements.items():
                contents = contents.replace(old_string, new_string)

            # Write the updated contents back to the file
            with open(file_path, "w") as f:
                f.write(contents)

print("Done!")
