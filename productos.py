import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Cargar los datos de Excel
df = pd.read_excel("/Users/ismartinez/Library/Mobile Documents/com~apple~CloudDocs/mdgt_files/site/mdgtlab/imprimex_productosseo.xlsx")

# Imprime los nombres de las columnas para verificar
print(df.columns)

# Configurar Jinja2 para cargar la plantilla
env = Environment(
    loader=FileSystemLoader(searchpath="./"),
    autoescape=select_autoescape(['html', 'xml'])
)

# Cargar la plantilla
template = env.get_template("plantilla.html")

# Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    # Intenta reemplazar espacios y caracteres especiales en el nombre del producto
    # para crear un nombre de archivo válido.
    try:
        nombre_archivo = row['page_title']
    except KeyError:
        # Si la columna no se encuentra, imprime un mensaje de error y salta al siguiente registro.
        print(f"Columna 'page_title' no encontrada para el índice {index}, se omite este registro.")
        continue

    # Divide la cadena de 'product_uses' en una lista usando comas como separador
    # Asegúrate de que 'product_uses' corresponde a una columna en tu Excel.
    product_uses = row['product_uses'].split(', ') if pd.notna(row['product_uses']) else []

    # Actualiza el diccionario de datos para la plantilla
    product_data = row.to_dict()
    product_data['product_uses'] = product_uses
    
    # Renderizar la plantilla con los datos del producto
    html_content = template.render(product_data)
    
    # Guardar el contenido en un nuevo archivo HTML
    # Asegúrate de que el nombre del archivo sea válido y único.
    with open(f"{nombre_archivo}.html", "w", encoding='utf-8') as f:
        f.write(html_content)