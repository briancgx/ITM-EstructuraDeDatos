class ColaDoble:
    def __init__(self):
        self.elements= []

    def estaVacia(self):
        return len(self.elements)==0

    def encolarFinal(self, dato):
        self.elements.append(dato)

    def encolarFrente(self, dato):
        self.elements.insert(0,dato)

    def desencolarFinal(self):
        try:
            return self.elements.pop()
        except IndexError:
            raise IndexError("Sin elementos en la cola")
        
    def desencolarFrente(self):
        try:
            return self.elements.pop(0)
        except IndexError:
            raise IndexError("Sin elementos en la cola")

    def tamanio(self):
        return len(self.elements)
    
    def showEle(self):
        print(self.elements)
