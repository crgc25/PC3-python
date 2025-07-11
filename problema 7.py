import random
from pyfiglet import Figlet

fonts_disponibles = Figlet.getFonts()

nombre_fuente = input("Ingrese el nombre de la fuente a utilizar (dejar en blanco para seleccionar aleatoriamente): ").strip()

if nombre_fuente and nombre_fuente in fonts_disponibles:
    fuente = nombre_fuente
else:
    fuente = random.choice(fonts_disponibles)
    print(f"No se ingresó una fuente válida. Se seleccionará aleatoriamente la fuente: {fuente}")

texto = input("Ingrese el texto que desea mostrar: ")

figlet = Figlet(font=fuente)

print(figlet.renderText(texto))
