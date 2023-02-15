def create_array(items):
    items_list = items.strip().split("\n")
    return items_list

items = """arte-revolucion-cesar-vallejo.md
circo-papel-alfaro.md
felisberto-casa-inundada.md
fermin-toro-martires.md
horacio-quiroga-cuentos.md
horacio-quiroga-cuentos-amor-locura.md
jotabeche-articulos.md
juguete-rabioso-arlt.md
lazarillo-ciegos-araujo.md
literatura-y-estetica-mariategui.md
martin-fierro-jose-hernandez.md
maria-jorge-isaacs.md
monja-casada-riva-palacio.md
nataniel-aguirre-juan-rosa.md
palma-tradiciones-peruanas-dos.md
poemas-humanos-vallejo-cesar.md
poemas-alfonsina-storni.md
poesias-completas-alfonso-moreno.md
simon-rodriguez-gonzalo-picon.md
tradiciones-peruanas-uno.md
anecdotario-froylan-turcios.md"""

array = create_array(items)
print(array)
