base_url = "https://morel.la/obras/"
urls = ["https://morel.la/obras/cuentos-quiroga",    "https://morel.la/obras/argentina-ruy-diaz-guzman",    "https://morel.la/obras/arte-revolucion-cesar-vallejo",    "https://morel.la/obras/circo-papel-alfaro",    "https://morel.la/obras/felisberto-casa-inundada",    "https://morel.la/obras/fermin-toro-martires",    "https://morel.la/obras/horacio-quiroga-cuentos",    "https://morel.la/obras/horacio-quiroga-cuentos-amor-locura",    "https://morel.la/obras/jotabeche-articulos",    "https://morel.la/obras/juguete-rabioso-arlt",    "https://morel.la/obras/lazarillo-ciegos-araujo",    "https://morel.la/obras/literatura-y-estetica-mariategui",
        "https://morel.la/obras/martin-fierro-jose-hernandez",    "https://morel.la/obras/maria-jorge-isaacs",    "https://morel.la/obras/monja-casada-riva-palacio",    "https://morel.la/obras/nataniel-aguirre-juan-rosa",    "https://morel.la/obras/palma-tradiciones-peruanas-dos",    "https://morel.la/obras/poemas-humanos-vallejo-cesar",    "https://morel.la/obras/poemas-alfonsina-storni",    "https://morel.la/obras/poesias-completas-alfonso-moreno",    "https://morel.la/obras/simon-rodriguez-gonzalo-picon",    "https://morel.la/obras/tradiciones-peruanas-uno",    "https://morel.la/obras/anecdotario-froylan-turcios"]

for url in urls:
    stripped_url = url.replace(base_url, '')
    modified_url = stripped_url + '.md'
    print(modified_url)
