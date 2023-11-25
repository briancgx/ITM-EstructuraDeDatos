class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def GetDato(self):
        return self.dato

    def GetSiguiente(self):
        return self.siguiente

    def SetDato(self, nuevoDato):
        self.dato = nuevoDato

    def SetSiguiente(self, nuevoSig):
        self.siguiente = nuevoSig

    def GetAnterior(self):
        return self.anterior

    def SetAnterior(self, nuevoAnt):
        self.anterior = nuevoAnt

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
            aux.SetSiguiente(nnodo)
            nnodo.SetAnterior(aux)
            self.ultimo = nnodo

        self.t += 1

    def RecorrerInicio(self):
        if not self.EstaVacia():
            nodo = self.primero
            datos = "["
            while nodo is not None:
                if nodo.GetSiguiente() is not None:
                    datos = datos + str(nodo.GetDato()) + ","
                    nodo = nodo.GetSiguiente()
                else:
                    datos = datos + str(nodo.GetDato()) + "]"
                    nodo = nodo.GetSiguiente()
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
            datos_persona = lista.primero
            while datos_persona is not None:
                print(f"Nombre: {datos_persona.GetDato()[0]}")
                print(f"Nacionalidad: {datos_persona.GetDato()[1]}")
                print(f"Fecha de Nacimiento: {datos_persona.GetDato()[2]}")
                print(f"Residencia: {datos_persona.GetDato()[3]}")
                print(f"CURP: {datos_persona.GetDato()[4]}")
                print()
                datos_persona = datos_persona.GetSiguiente()
            print()

def main():
    lista_circular = ListaCircular()

    datos_personas = []
    for i in range(3):
        datos_persona = []
        nombre = input(f"Nombre de la persona {i + 1}: ")
        nacionalidad = input(f"Nacionalidad de la persona {i + 1}: ")
        fecha_nacimiento = input(f"Fecha de Nacimiento de la persona {i + 1}: ")
        residencia = input(f"Residencia de la persona {i + 1}: ")
        curp = input(f"CURP de la persona {i + 1}: ")
        datos_persona.extend([nombre, nacionalidad, fecha_nacimiento, residencia, curp])
        datos_personas.append(datos_persona)

    for i, datos_persona in enumerate(datos_personas):
        lista_circular.AgregarPersona(datos_persona, i)

    lista_circular.ImprimirPersonas()

if __name__ == "__main__":
    main()