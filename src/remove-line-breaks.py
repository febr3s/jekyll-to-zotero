import os

def remove_initial_linebreak(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()

    new_contents = contents.lstrip('\n')

    with open(file_path, 'w') as f:
        f.write(new_contents)

def main():
    folder_path = '/home/febres/Documents/dev/100DaysOfCode/0-Ch_1-_Orinales_fuera_de_sus_casillas' # Replace with the path to the folder you want to process
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                remove_initial_linebreak(file_path)

if __name__ == '__main__':
    main()
