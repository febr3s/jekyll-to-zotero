import os

folder_path = "/home/febres/Documents/dev/morelcoop.github.io/_books"  # replace with the path to your folder
line_to_delete = "feature:"  # replace with the line you want to delete

# loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # check if the file is a text file
    if file_path.endswith(".md"):
        # read the file into a list of lines
        with open(file_path, "r") as file:
            lines = file.readlines()

        # remove the line to delete
        with open(file_path, "w") as file:
            for line in lines:
                if line.strip() != line_to_delete:
                    file.write(line)
                    
        print(f"{filename}: Line deleted.")
    else:
        print(f"{filename}: Not a text file.")