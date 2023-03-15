import csv

# Set the name of the input CSV file
input_file = "/home/febres/Documents/dev/100DaysOfCode/list-quotes.csv"

# Set the name of the output CSV file
output_file = "/home/febres/Documents/dev/100DaysOfCode/list-quotes.csv"

# Read the data from the input CSV file
with open(input_file, "r") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

# Modify the data by adding ";;" to the beginning of each word in the first column
for row in rows:
    row[1] = "@" + row[1]

# Write the modified data to the output CSV file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
