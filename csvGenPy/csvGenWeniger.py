import pandas as pd
import random


brands_with_types = {
    'Coca-Cola': ['Alkoholfreies Getränk'],
    'Vöslauer': ['Alkoholfreies Getränk'],
    'Stiegl': ['Bier'],
    'Alpenmilch': ['Milch'],
    'Gruber\'s': ['Mehl'],
    'Südzucker': ['Zucker'],
    'Milka': ['Schokolade'],
    'Haribo': ['Gummibärchen']
}

packaging_with_materials = {
    'Flasche': ['Glas', 'PET'],
    'Dose': ['Alu'],
    'Tetra Pak': ['Papier'],
    'Papierbeutel': ['Papier'],
   
    'Plastikbeutel': ['Plastik']
}

sizes_with_types = {
    'Alkoholfreies Getränk': ['0,25 LT', '0,5 LT', '1 LT', '1,5 LT'],
    'Bier': ['0,5 LT', '1 LT'],
    'Milch': ['0,5 LT', '1 LT', '1,5 LT'], 
    'Mehl': ['0,5kg', '1kg'], 
    'Zucker': ['0,5kg', '1kg'],  
    'Schokolade': ['100g', '200g', '300g'], 
    'Gummibärchen': ['100g', '200g', '300g'],
}


products = []
products_set = set()  

for _ in range(100):
    brand, product_types = random.choice(list(brands_with_types.items()))
    product_type = random.choice(product_types)
    verpackungsart, materials = random.choice(list(packaging_with_materials.items()))
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


df.to_csv('ItemsWenigerLogik.csv', index=False, encoding='utf-8-sig')