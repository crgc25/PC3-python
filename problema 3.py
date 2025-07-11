class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        pi = 3.141592653589793
        return pi * (self.radio ** 2)

# Crear dos objetos de tipo CIRCULO
circulo1 = CIRCULO(5)
circulo2 = CIRCULO(10)

print(f"Área del círculo 1: {circulo1.calcular_area()}")
print(f"Área del círculo 2: {circulo2.calcular_area()}")
