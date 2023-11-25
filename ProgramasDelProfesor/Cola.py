class Cola:
    def __init__(self):#constructor de la clase Cola
        self.fila=[] 
        
    def encolar(self, data):
        self.fila.append(data)
        
    def desencolar(self):
        try: #bloque de sentencias que podrían generar una excepción
            return self.fila.pop(0)
        except IndexError: #bloque para manejar la excepción
            print ("Sin elementos en la cola")

  
    def estaVacia(self):
        return len(self.fila)==0 #si está vacía devuelve True, de lo contrario devuelve False
    
    def vaciar(self):
        del self.fila[:] #la función del se emplea para 
        
    def frente(self):
        try:
            return self.fila[0]#devuelve el ultimo elemento que ingreso a la lista
        except IndexError:
            print ("Sin elementos en la cola")
    def final (self):
        try:
            return self.fila[-1]
        except IndentationError:
            print("sin elementos en la cola")
    def tamanio(self):
        return len(self.fila)
    def showEl(self):
        print("Elementos de la pila:\n",self.fila)
# c=Cola()
# c.encolar("Josh")
# c.encolar("Maria")
# c.showEl()
# c.desencolar()
# c.showEl()