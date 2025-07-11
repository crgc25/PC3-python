class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.nota = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        else:
            print("Edad: No asignada")
        if self.nota is not None:
            print(f"Nota: {self.nota}")
        else:
            print("Nota: No asignada")
    
    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, nota):
        self.nota = nota

alumno1 = Alumno("Freddy Sina", 322)
alumno1.setAge(34)
alumno1.setNota(18.5)
alumno1.display()
