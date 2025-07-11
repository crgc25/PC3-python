ef main():
    while True:
        try:
            fraccion = input("Ingrese la fracción en formato X/Y: ").strip()
            if '/' not in fraccion:
                print("Error: El formato debe ser X/Y.")
                continue

            X_str, Y_str = fraccion.split('/')
            X = int(X_str)
            Y = int(Y_str)

            if Y == 0:
                print("Error: Y no puede ser cero.")
                continue
            if X < 0 or Y < 0:
                print("Error: X y Y deben ser números enteros positivos.")
                continue
            if X > Y:
                print("Error: X debe ser menor o igual a Y.")
                continue

            porcentaje = (X / Y) * 100
            porcentaje_redondeado = round(porcentaje)

            if porcentaje < 1:
                resultado = 'E'
            elif porcentaje > 99:
                resultado = 'F'
            else:
                resultado = f"{porcentaje_redondeado}%"

            print(f"Cantidad de combustible en el tanque: {resultado}")
            break 

        except ValueError:
            print("Error: X y Y deben ser números enteros.")
        except ZeroDivisionError:
            print("Error: División por cero detectada, Y no puede ser cero.")

if __name__ == "__main__":
    main()
