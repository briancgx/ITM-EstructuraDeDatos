# Brian Azael Cumi Guzman 3SA

class UsoDeColas:
    def __init__(self):
        self.fila = []
        self.tamanio = 0

    def encolar(self, data, al_frente=False):
        if al_frente:
            self.fila.insert(0, data)
        else:
            self.fila.append(data)
        self.tamanio += 1

    def desencolar(self, del_frente=True):
        if not self.esta_vacia():
            self.tamanio -= 1
            if del_frente:
                return self.fila.pop(0)
            else:
                return self.fila.pop()
        else:
            return None

    def esta_vacia(self):
        return self.tamanio == 0

    def mostrar(self):
        return self.fila
    
entrada_cadena1 = input("Entrada cadena 1 (separada por comas): ").split(',')
entrada_cadena2 = input("Entrada cadena 2 (separada por comas): ").split(',')

cola_simple_original = UsoDeColas()
cola_doble_original = UsoDeColas()

for num in entrada_cadena1:
    cola_simple_original.encolar(int(num))

for num in entrada_cadena2:
    cola_doble_original.encolar(int(num))

cola_simple_copia = UsoDeColas()
cola_simple_copia.fila = cola_simple_original.fila.copy()
cola_doble_copia = UsoDeColas()
cola_doble_copia.fila = cola_doble_original.fila.copy()

cola_circular = UsoDeColas()

while not cola_simple_original.esta_vacia() and not cola_doble_original.esta_vacia():
    suma = cola_simple_original.desencolar() + cola_doble_original.desencolar()
    cola_circular.encolar(suma)

print("cola simple:", cola_simple_copia.mostrar())
print("cola doble:", cola_doble_copia.mostrar())
print("Salida (cola circular):", cola_circular.mostrar())

cola_simple_original.fila = []
cola_doble_original.fila = []