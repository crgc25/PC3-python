import requests
import zipfile
import os

url_imagen = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'  
nombre_archivo_imagen = 'imagen.jpg'

try:
    response = requests.get(url_imagen)
    response.raise_for_status()
    with open(nombre_archivo_imagen, 'wb') as f:
        f.write(response.content)
    print(f'Imagen descargada y guardada como {nombre_archivo_imagen}')
except requests.exceptions.RequestException as e:
    print(f'Error al descargar la imagen: {e}')

nombre_zip = 'imagen_comprimida.zip'
with zipfile.ZipFile(nombre_zip, 'w') as zipf:
    zipf.write(nombre_archivo_imagen)
print(f'Imagen comprimida en {nombre_zip}')

directorio_descompresion = 'descomprimido'
os.makedirs(directorio_descompresion, exist_ok=True)

with zipfile.ZipFile(nombre_zip, 'r') as zipf:
    zipf.extractall(directorio_descompresion)
print(f'Archivo descomprimido en la carpeta {directorio_descompresion}')
