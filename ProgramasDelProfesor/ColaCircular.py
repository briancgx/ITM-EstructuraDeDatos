class ColaCircular:
    def __init__(self, t):
        self.max=t #número máximo de elementos de la cola
        self.colacirc=[] #se inicializa la lista
        self.n=0 #número de elementos actuales en la cola circular
        self.frente=0 #posición de incio de la cola
        for i in range (self.max): #se asigna None en los valores de la cola
            self.colacirc.append(None)
            
    def Encolar(self,dato):
        if self.n!=self.max: #si la cola no se ha llenado entonces se procede a agregar elementos
            self.pos=(self.frente+self.n)%self.max #se calcula la posicion del dato a ingresar
            self.colacirc[self.pos]=dato #se agrega el dato a la cola circular
            self.n=self.n+1 #se incrementa el número de elementos en la cola
            print("frente: ",self.frente," n ", self.n,"maximo: ",self.max," pos: ", self.pos)
        else:
            print("Cola circular llena")
            
    def Desencolar(self): 
        if not self.estaVacia(): #si la cola circular no está vacía, entonces:
            salida=self.colacirc[self.frente] #se obtiene el elemento de la posición de frente
            self.colacirc[self.frente]=None #el elemento ahora es None
            self.n=self.n-1 #se decrementa el número de elementos en la cola
            self.frente=(self.frente+1)%self.max #se calcula la nueva posición de frente
            #print("frente: ",self.frente, "n: ",self.n)
            return salida #se retorna el valor
        print("La cola circular esta vacia")
        return None

    def estaVacia(self):
        #print(self.n)
        return self.n==0
    
    def showEl(self):
        print(self.colacirc)
        
    def vaciar(self):
        for i in range (self.max):
            self.colacirc[i]=None
        self.n=0
        
    def primero(self):
        if not self.estaVacia():
            return self.colacirc[self.frente]
        print("La cola circular esta vacia")
        return None
    
    def ultimo(self):
        if not self.estaVacia():
            return self.colacirc[self.pos]
        print("La cola circular esta vacia")
        return None    
    
    def tamanio(self):
        return (self.frente+self.n)-1
    
cc=ColaCircular(20)
cc.Encolar(1)
cc.Encolar(8)
cc.showEl()