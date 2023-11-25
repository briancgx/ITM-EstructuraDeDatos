class Pila:

    def __init__(self):
        self.el=[]
       
    def Push(self, data):
        self.el.append(data)
        
    def Pop(self):
        try:
            return self.el.pop()
        except IndexError:
            print ("Pila vacia")

    def estaVacia(self):
        return len(self.el)==0 #devuelve un True si la lista está vacía, de los contrario devuelve False
    
    def vaciar(self):
        del self.el[:] #elimina todos los elementos de la pila
        
    def top(self):
        try:# bloque que podría generar una excepción
            return self.el[-1] #devuelve el elemento de la última posición: posición (0-1)
        except IndexError: #bloque para manejar la excepción
            print ("Pila vacia")
            
    def tamanio(self):
        return len(self.el)
    
    def showEl(self):
        print("Elementos de la pila:\n",self.el)
# p=Pila()
# p.Push("a")
# p.Push("b")
# p.Push("c")
# p.Push("d")
# p.Push("e")
# p.showEl()
# p.Pop()
# p.showEl()
# p.vaciar()
# p.showEl()