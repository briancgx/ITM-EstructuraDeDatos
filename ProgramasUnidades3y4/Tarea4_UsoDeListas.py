class Persona:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, residencia, curp):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.residencia = residencia
        self.curp = curp

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.t = 0

    def EstaVacia(self):
        return self.primero is None

    def AgregarUltimo(self, dato):
        if self.EstaVacia():
            self.ultimo = Nodo(dato)
            self.primero = self.ultimo
        else:
            aux = self.ultimo
            nnodo = Nodo(dato)
            aux.siguiente = nnodo
            nnodo.anterior = aux
            self.ultimo = nnodo

        self.t += 1

    def RecorrerInicio(self):
        if not self.EstaVacia():
            nodo = self.primero
            datos = "["
            while nodo is not None:
                if nodo.siguiente is not None:
                    datos += f"Nombre: {nodo.dato.nombre}, "
                    nodo = nodo.siguiente
                else:
                    datos += f"Nombre: {nodo.dato.nombre}]"
                    nodo = nodo.siguiente
            print(datos)
        else:
            print("Lista vacía")

class ListaCircular:
    def __init__(self):
        self.listas = [ListaDoblementeEnlazada() for _ in range(3)]

    def AgregarPersona(self, datos, indice):
        self.listas[indice].AgregarUltimo(datos)

    def ImprimirPersonas(self):
        for i, lista in enumerate(self.listas):
            print(f"Persona {i + 1}:")
            nodo = lista.primero
            while nodo is not None:
                persona = nodo.dato
                print(f"Nombre: {persona.nombre}")
                print(f"Nacionalidad: {persona.nacionalidad}")
                print(f"Fecha de Nacimiento: {persona.fecha_nacimiento}")
                print(f"Residencia: {persona.residencia}")
                print(f"CURP: {persona.curp}")
                print()
                nodo = nodo.siguiente
            print()

def main():
    lista_circular = ListaCircular()

    for i in range(3):
        nombre = input(f"Nombre de la persona {i + 1}: ")
        nacionalidad = input(f"Nacionalidad de la persona {i + 1}: ")
        fecha_nacimiento = input(f"Fecha de Nacimiento de la persona {i + 1}: ")
        residencia = input(f"Residencia de la persona {i + 1}: ")
        curp = input(f"CURP de la persona {i + 1}: ")
        persona = Persona(nombre, nacionalidad, fecha_nacimiento, residencia, curp)
        lista_circular.AgregarPersona(persona, i)

    lista_circular.ImprimirPersonas()

if __name__ == "__main__":
    main()

# Brian Azael Cumi Guzman 3SA