class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None
    def GetDato(self):
        return self.dato
    def GetSiguiente(self):
        return self.siguiente
    def SetDato(self,nuevoDato):
        self.dato=nuevoDato
    def SetSiguiente(self,nuevoSig):
        self.siguiente=nuevoSig
        
class ListaCircular():
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.t=0
    def EstaVacia(self):
        return self.primero==None
    def AgregarInicio(self, dato):        
        if self.EstaVacia():
            self.primero=Nodo(dato)
            self.ultimo=self.primero #Ya que no hay elementos en la lista, el primer elemento y el ultimo son el mismo nodo
            self.ultimo.SetSiguiente(self.primero) #El ultimo nodo apunta al primero
        else:
            nodo=Nodo(dato)
            nodo.SetSiguiente(self.primero) #El nodo siguiente del que se añadió es el que era el primero
            self.primero=nodo #Ahora el primer nodo es el nuevo
            self.ultimo.SetSiguiente(self.primero) #El ultimo nodo apunta al nuevo que se creó
        self.t+=1
    def AgregarUltimo(self, dato):
        if self.EstaVacia():
            #print(dato)
            self.primero=Nodo(dato)
            self.ultimo=self.primero #Ya que no hay elementos en la lista, el primer y ultimo elemento son el nodo que se creó
            self.ultimo.SetSiguiente(self.primero) #el ultimo nodo apunta al primero
        else:
            ultnodo=self.ultimo #Almacena el ultimo nodo
            nnodo=Nodo(dato)  #Se crea un nodo
            ultnodo.SetSiguiente(nnodo) #El ultimo nodo apunta al nuevo
            self.ultimo=nnodo #El nodo que se creo ahora será el último
            self.ultimo.SetSiguiente(self.primero) #El nuevo nodo apunta al primero
        self.t+=1
            
    def Show(self):
        if not self.EstaVacia():
            nodo=self.primero
            print(nodo.GetDato())
            nodo=nodo.GetSiguiente()
            while nodo!=self.primero:
                print(nodo.GetDato())
                nodo=nodo.GetSiguiente()    
        else:
            print("Lista Vacia")
    def GetNodo(self, pos):
        if not self.EstaVacia():        
                if(pos<self.t) & (pos>=0):
                    c=0
                    nodo=self.primero
                    while c<=pos:
                        aux=nodo
                        nodo=nodo.GetSiguiente()
                        c+=1
                    return aux.GetDato()
                else:
                   print("Fuera de los índices de la lista")
                   
        else:
            print("Lista vacia")
        return None
    def SetNodo(self, pos, dato):
        if not self.EstaVacia():        
                if(pos<self.t) & (pos>=0):
                    c=0
                    nodo=self.primero
                    while c<=pos:
                        aux=nodo
                        nodo=nodo.GetSiguiente()
                        c+=1
                    aux.SetDato(dato)
                else:
                   print("Fuera de los índices de la lista")
                   
        else:
            print("Lista vacia")
    def GetPrimero(self):
        if not self.EstaVacia():
            return self.primero.GetDato()
        print("Lista Vacia")
        return None
    def GetUltimo(self):
        if not self.EstaVacia():
            return self.ultimo.GetDato()
        print("Lista Vacia")
        return None
    def Insertar(self, pos,dato):
        if not self.EstaVacia():        
            if pos==0:
                nodo=Nodo(dato)
                nodo.SetSiguiente(self.primero)
                self.primero=nodo
                self.ultimo.SetSiguiente(self.primero)
                self.t+=1
            else:
                if(pos<self.t) & (pos>=0):
                    c=0
                    nodo=self.primero
                    while c<pos:
                        aux=nodo
                        nodo=nodo.GetSiguiente()
                        c+=1
                    nnodo=Nodo(dato)
                    aux.SetSiguiente(nnodo)
                    nnodo.SetSiguiente(nodo)
                    self.t+=1
                else:
                   print("Fuera de los índices de la lista") 
        else:
            print("Lista vacia")
    def EliminarNodo(self, pos):
        if not self.EstaVacia():        
            if pos==0:
                nodo=self.primero.GetSiguiente()
                self.primero=nodo
                self.ultimo.SetSiguiente(self.primero)
                self.t-=1
            else:
                if(pos<self.t) & (pos>=0):
                    c=0
                    nodo=self.primero
                    while c<pos:
                        aux=nodo
                        nodo=nodo.GetSiguiente()
                        c+=1
                    if nodo==self.ultimo:
                        self.ultimo=aux
                        self.ultimo.SetSiguiente(self.primero)
                    else:
                        aux.SetSiguiente(nodo.GetSiguiente())
                    self.t-=1
                else:
                   print("Fuera de los índices de la lista")
            if self.t==0:
                self.primero=None
                self.ultimo=None
        else:
            print("Lista vacia")
            
    def Eliminar(self, dato):
        if not self.EstaVacia():
            nodo=self.primero
            encontrado=False
            if nodo.GetDato()==dato:
                    encontrado=True
            #print(nodo.GetDato())
            c=0
            while (not encontrado) & (c<self.t):
                aux=nodo
                nodo=nodo.GetSiguiente() 
                
                if nodo.GetDato()==dato:
                    encontrado=True
                    #print(nodo.GetDato())
                c+=1
            if encontrado:        
                if nodo==self.primero:
                    nodo=self.primero.GetSiguiente()
                    self.primero=nodo
                    self.ultimo.SetSiguiente(self.primero)
                    #self.t-=1
                elif nodo==self.ultimo:
                    self.ultimo=aux
                    self.ultimo.SetSiguiente(self.primero)
                else:
                    aux.SetSiguiente(nodo.GetSiguiente())
                self.t-=1
                if self.t==0:
                    self.primero=None
                    self.ultimo=None
            else:
                print("No se encontro el elemento")
        else:
            print("Lista vacia")
    def Tamanio(self):
        return self.t
    def ElDatosLista(self):
        self.primero=None
        self.ultimo=None
        self.t=0