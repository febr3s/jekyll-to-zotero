import os
import csv
import string
from collections import Counter

# Set the directory to search for markdown files
directory = "/home/febres/Documents/dev/100DaysOfCode/0-Ch_1-_Orinales_fuera_de_sus_casillas"

# Set the name of the output CSV file
output_file = "/home/febres/Documents/dev/100DaysOfCode/0-Ch_1-_Orinales_fuera_de_sus_casillas/list-quotes.csv"

# Create a string containing all punctuation marks
punctuation = string.punctuation

# Create an empty list to store the words found in the markdown files
words_list = []

# Loop through each markdown file in the directory and its subdirectories
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            # Read the contents of the file
            with open(os.path.join(subdir, file), "r") as f:
                contents = f.read()

            # Extract all the words that start with ";;" or "[;;" from the markdown
            words = [word.translate(str.maketrans("", "", punctuation)) for word in contents.split() if word.startswith(";;") or word.startswith("[;;")]

            # Add the words to the list
            words_list.extend(words)

# Count the number of times each word appears in the list
word_counts = Counter(words_list)

# If the output file already exists, read in the existing data
if os.path.exists(output_file):
    with open(output_file, "r") as f:
        reader = csv.reader(f)
        existing_data = {row[0]: int(row[1]) for row in reader}
else:
    existing_data = {}

# Write the word counts to the output CSV file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    for word, count in word_counts.items():
        # Remove punctuation marks from the word
        word = word.translate(str.maketrans("", "", punctuation))

        # If the word already exists in the output file, update the count
        if word in existing_data:
            count += existing_data[word]

        # Write the word and count to the output file
        writer.writerow([word, count])
