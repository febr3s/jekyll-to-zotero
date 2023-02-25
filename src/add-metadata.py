import os

# List of specific files to process
files_to_process = ['cantos-primaverales.md', 'canto-samuel-lillo.md', 'calices-vacios-delmira.md', 'el-dulce-dano-astorni.md', 'altazor-huidobro.md', 'obras-completas-tomo-ii.md', 'poesia-ruben-dario.md', 'albores-carlos-augusto-salaverry.md', 'alma-idilio.md', 'ambrogi-tiempo-que-pasa.md', 'angel-polibio-versos.md', 'antologia-delmira-agustini.md', 'aquileo-echeverria-romances.md', 'aquileo-echeverr%C3%ADa-concherias.md', 'araucana-ercilla-cuatro.md', 'araucana-ercilla-dos.md', 'araucana-ercilla-tres.md', 'arauco-domado-pedro-o%C3%B1a.md', 'armas-antarticas-miramontes.md', 'articulos-poesias-comedias.md', 'astros-abismo-delmira.md', 'bello-poesias.md', 'blanca-luz-juan-parra-riego.md', 'demetrio-herrera-antologia.md', 'deshojando-silencio-mendilaharsu.md', 'diaz-guerra-inundacion.md', 'dolores-veintimilla-produccion.md', 'domador-pulgas.md', 'espana-cesar-vallejo.md', 'felipe-pardo-poesia.md', 'gertrudis-gomez-poesias.md', 'franz-tamayo-obra.md', 'golgota-felix-antonio.md', 'gruta-silencio-vicente-huidobro.md', 'heredia-poesias-liricas.md', 'guzman-papini-la-novia.md', 'guirnalda-salvadorena.md', 'horno-jose-cuadra.md', 'inquietud-luisa-luisi.md', 'isla-canticos-maria-eugenia-vaz-ferreira.md', 'ignacio-manuel-altamirano.md', 'jose-asuncion-silva.md', 'jose-batres-poesias.md', 'julian-casal-nieve.md', 'languidez-alfonsina-storni.md', 'leonardo-eliz-posias-liricas.md', 'leyendas-mayas-manuel-rejon-garcia.md', 'libro-fiel-leopoldo-lugones.md', 'lillo-sub-terra.md', 'carriego-misas-herejes.md', 'castalia-barbara-ricardo-freyre.md', 'cautiva-esteban-echeverria.md', 'celajes-cordillera-merlos-salvador.md', 'cencerro-cristal-ricardo.md', 'cien-carceles-amor.md', 'cien-sonetos-serrano-francisco.md', 'circo-papel-alfaro.md', 'cofre-psiquis.md', 'como-nubes-mendilaharsu.md', 'poesias-completas-alfonso-moreno.md', 'poesias-completas-jorge-isaacs.md', 'poesias-domingo-estrada.md', 'poesias-escogidas.md', 'poesias-evaristo.md', 'poesias-gabriel-concepcion.md', 'poesias-ignacio-rodriguez.md', 'poesias-independencia.md', 'poesias-jocosas-cordero.md', 'poesias-jose-asuncion.md', 'poesias-luis-montt.md', 'poesias-rodulfo-figueroa.md', 'poesias-rogelio-fernandez-guell.md', 'poesias-salome.md', 'poes%C3%ADa-prosa-julian-casal.md', 'pedro-arismendi-versos.md', 'pedro-requena-legarreta.md', 'poemas-alfonsina-storni.md', 'poemas-helenicos-goycochea.md', 'poemas-humanos-vallejo-cesar.md', 'poemas-sinfonicos.md', 'manojo-guarias-chavarria.md', 'manuel-gutierrez-poesias.md', 'noboa-ernesto-romanza.md', 'obras-escogidas-jose-eusebio-caro.md', 'obras-poeticas-jose-olmedo.md', 'pais-memoria-susana-soca.md', 'pascuas-tiempo-herrera-reissig.md', 'zamudio-adela-misionero.md', 'voces-intimas.md', 'vicu%C3%B1a-cifuentes.md', 'vibraciones-ignacio-valdes.md', 'viaje-nicaragua-ruben-dario.md', 'versos-criollos-elias-regules.md', 'versos-carlos-roxlo.md', 'versos-bustillo.md', 'torre-timon-ramos-sucre.md', 'surtidores-josefina-penate.md', 'sue%C3%B1os-mundo-ruben-dario.md', 'suenos-zulima.md', 'sor-juana-poesias-escogidas.md', 'sor-juana-cruz.md', 'sonetos-sonetillos-trajano-mera.md', 'sentir-luisa-luisi.md', 'sataniada-alejandro-tapia.md', 'santiago-arguello-poema-locura.md', 'sabados-mayo.md', 'ruben-dario-prosa-dispersa.md', 'ruben-dario-otono.md', 'ruben-dario-azul.md', 'rosas-mercedes-gonzalez.md', 'rimas-bartolome-mitre.md', 'pregon-marimorena-virginia-brindis.md', 'revenar-max-jimenez.md', 'prosas-profanas-ruben-dario.md', 'prosa-susana-soca.md', 'popol-vuh.md', 'polvo-dias-luisa-luisi.md', 'polirritmos-juan-parra-riego.md']

# Directory containing the .md files
directory = "/home/febres/Documents/dev/morelcoop.github.io/_books"

# Loop through the specified files
for filename in files_to_process:
    file_path = os.path.join(directory, filename)
    
    # Check if the file exists in the directory
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        # Human: replace "periodo" with the one that is right before the metadata container that you want to add and/or modify in bulk
        # Check if the "periodo:" line is present in the file

        periodo_line = None
        for i, line in enumerate(lines):
            if line.startswith("periodo:"):
                periodo_line = i
                break
        
        # Human: replace "featured" with the metadata container that you want to add and/or modify in bulk, and replace "false" with the respective value
        # If the "periodo:" line was found, insert the "genre: poetry\n" line right after it if it doesn't already exist

        if periodo_line is not None:
            if "genre: poetry\n" not in lines:
                lines.insert(periodo_line + 1, "genre: poetry\n")
        
        # Write the updated file content
        with open(file_path, "w") as file:
            file.writelines(lines)
    else:
        print(f"{filename} not found in {directory}.")
