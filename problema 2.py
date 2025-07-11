calificaciones_input = input("Ingrese una lista de calificaciones separadas por comas: ")

calificaciones_str = calificaciones_input.split(',')

calificaciones = []

for cal in calificaciones_str:
    cal = cal.strip()
    try:
        cal_int = int(cal)
        calificaciones.append(cal_int)
    except ValueError:
        print(f"Valor inválido de calificación: '{cal}'. No se pudo convertir a número entero.")

print("Lista de calificaciones válidas:", calificaciones)
