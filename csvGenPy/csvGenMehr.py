import pandas as pd
import random


brands_with_types = {
    'Coca-Cola': ['Alkoholfreies Getränk'],
    'Vöslauer': ['Alkoholfreies Getränk'],
    'Stiegl': ['Bier'],
    'Gösser': ['Bier'],
    'Alpenmilch': ['Milch'],
    'Nöm': ['Milch'],
    'Gruber\'s': ['Mehl'],
    'Zielpunkt': ['Mehl'],
    'Südzucker': ['Zucker'],
    'Agrana': ['Zucker'],
    'Milka': ['Schokolade'],
    'Zotter': ['Schokolade'],
    'Haribo': ['Gummibärchen'],
    'Manner': ['Snacks'],
    'Darbo': ['Marmelade']
}

packaging_options = {
    'Alkoholfreies Getränk': [('Flasche', ['Glas', 'PET']), ('Dose', ['Alu'])],
    'Bier': [('Flasche', ['Glas']), ('Dose', ['Alu'])],
    'Milch': [('Tetra Pak', ['Papier']), ('Flasche', ['Glas', 'PET'])],
    'Mehl': [('Papierbeutel', ['Papier']), ('Plastikbeutel', ['Plastik'])],
    'Zucker': [('Papierbeutel', ['Papier']), ('Plastikbeutel', ['Plastik'])],
    'Schokolade': [('Papierbeutel', ['Papier'])],
    'Gummibärchen': [('Papierbeutel', ['Papier']), ('Plastikbeutel', ['Plastik'])],
    'Snacks': [('Papierbeutel', ['Papier']), ('Plastikbeutel', ['Plastik'])],
    'Marmelade': [('Glas', ['Glas'])]
}

sizes_with_types = {
    'Alkoholfreies Getränk': ['0,25 LT', '0,5 LT', '1 LT', '1,5 LT'],
    'Bier': ['0,33 LT', '0,5 LT', '1 LT'],
    'Milch': ['0,5 LT', '1 LT', '1,5 LT'],
    'Mehl': ['0,5kg', '1kg', '2kg'],
    'Zucker': ['0,5kg', '1kg', '2kg'],
    'Schokolade': ['100g', '200g', '300g'],
    'Gummibärchen': ['100g', '200g', '300g'],
    'Snacks': ['150g', '300g'],
    'Marmelade': ['250g', '500g']
}

products = []
products_set = set()

for _ in range(100):
    brand, product_types = random.choice(list(brands_with_types.items()))
    product_type = random.choice(product_types)
    verpackungsart, materials = random.choice(packaging_options[product_type])
    material = random.choice(materials)
    size = random.choice(sizes_with_types[product_type])

    product_name = f"{brand} {product_type} {size} {material} {verpackungsart}"

    if product_name not in products_set:
        product = {
            'Produktname': product_name,
            'Marke': brand,
            'Produktart': product_type,
            'Verpackungsart': verpackungsart,
            'Material': material,
            'Größe': size
        }
        products.append(product)
        products_set.add(product_name)

df = pd.DataFrame(products)
df.to_csv('ItemsMehrLogik.csv', index=False, encoding='utf-8-sig')

print("CSV-Datei wurde erfolgreich erstellt.")
