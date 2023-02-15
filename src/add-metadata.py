import os

# List of specific files to process
files_to_process = [    "Cuentos-Quiroga.md",    "argentina-ruy-diaz-guzman.md",    "arte-revolucion-cesar-vallejo.md",    "circo-papel-alfaro.md",    "felisberto-casa-inundada.md",    "fermin-toro-martires.md",    "horacio-quiroga-cuentos.md",    "horacio-quiroga-cuentos-amor-locura.md",    "jotabeche-articulos.md",    "juguete-rabioso-arlt.md",    "lazarillo-ciegos-araujo.md",    "literatura-y-estetica-Mariategui.md",    "martin-fierro-jose-hernandez.md",    "maria-jorge-isaacs.md",    "monja-casada-riva-palacio.md",    "nataniel-aguirre-juan-rosa.md",    "palma-tradiciones-peruanas-dos.md",    "poemas-humanos-vallejo-cesar.md",    "poemas-alfonsina-storni.md",    "poesias-completas-alfonso-moreno.md",    "simon-rodriguez-gonzalo-picon.md",    "tradiciones-peruanas-uno.md",    "anecdotario-froylan-turcios.md"]


# Directory containing the .md files
directory = "/home/febres/Documents/dev/morelcoop.github.io/_books"

# Loop through the specified files
for filename in files_to_process:
    file_path = os.path.join(directory, filename)
    
    # Check if the file exists in the directory
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        # Check if the "periodo:" line is present in the file
        periodo_line = None
        for i, line in enumerate(lines):
            if line.startswith("periodo:"):
                periodo_line = i
                break
        
        # If the "periodo:" line was found, insert the "featured: false" line right after it
        if periodo_line is not None:
            lines.insert(periodo_line + 1, "featured: false\n")
        
        # Write the updated file content
        with open(file_path, "w") as file:
            file.writelines(lines)
    else:
        print(f"{filename} not found in {directory}.")
