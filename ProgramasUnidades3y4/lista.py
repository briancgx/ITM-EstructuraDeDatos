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
        
class ListaEnlazada:
    def __init__(self):
        self.primero=None
        #print(self.primero)
        self.t=0
    def EstaVacia(self):
        return self.primero==None
    def AgregarPrimero(self,dato):
        nodo=Nodo(dato)
        #print(self.primero)
        nodo.SetSiguiente(self.primero)
        self.primero=nodo
        self.t=self.t+1
    def AgregarUltimo(self,dato):
        nodo=Nodo(dato)
        nodo.SetSiguiente(None)
        if self.EstaVacia():
            self.primero=nodo
        else:
            aux=self.primero
            while aux!=None:
                anterior=aux
                aux=aux.GetSiguiente()
            anterior.SetSiguiente(nodo)
        self.t=self.t+1
        
    def Tamanio(self):
        return self.t
    
    def insertar(self, pos,dato):
        if not self.EstaVacia():        
            if pos==0:
                nodo=Nodo(dato)
                nodo.SetSiguiente(self.primero)
                self.primero=nodo
                self.t=self.t+1
            else:
            #print("no vacia")

                nodo=self.primero
                if(pos <self.t) & (pos>=0):
                    c=0
                    while (nodo!=None) & (c<pos):
                        aux=nodo
                        nodo=nodo.GetSiguiente()
                        c+=1
                    #aux.SetDato(dato)
                    nnodo=Nodo(dato)
                    aux.SetSiguiente(nnodo)
                    nnodo.SetSiguiente(nodo)
                    self.t=self.t+1
                else:
                    print("Fuera de los índices de la lista")
        else:
            print("Lista vacia")  
            
    def Show(self):
        if not self.EstaVacia():
            nodo=self.primero
            datos="["
            while nodo!=None:
                if(nodo.GetSiguiente()!=None):
                    datos=datos+str(nodo.GetDato())+","
                    nodo=nodo.GetSiguiente()
                else:
                    datos=datos+str(nodo.GetDato())+"]"
                    nodo=nodo.GetSiguiente()
            print(datos)
        else:
            print("Lista vacia")
            
    def Eliminar(self,dato):
        if not self.EstaVacia():
            nodo=self.primero
            anterior=None
            encontrado=False
            while not encontrado and nodo!=None:
                if(nodo.GetDato()==dato):
                    encontrado=True
                else:
                    anterior=nodo
                    nodo=nodo.GetSiguiente()
            if not encontrado:
                print("No se encontro")
            else:
                if anterior==None:
                    self.primero=nodo.GetSiguiente()
                    print("ocurrio")
                else:
                    anterior.SetSiguiente(nodo.GetSiguiente())
                self.t=self.t-1
            if self.t==0:
                self.primero=None
        else:
            print("lista vacia")
            
    def SetNodo(self,pos,dato):
        if not self.EstaVacia():
            nodo=self.primero
            if(pos <self.t) & (pos>=0):
                c=0
                while (nodo!=None) & (c<=pos):
                    aux=nodo
                    nodo=nodo.GetSiguiente()
                    c+=1
                #print(pos)
                #print(aux.GetDato())
                aux.SetDato(dato)
            else:
                print("Fuera de los índices de la lista")
        else:
            print("Lista vacia")
            
    def GetNodo(self,pos):
        if not self.EstaVacia():
            nodo=self.primero
            if (pos <self.t) & (pos>=0):
                c=0
                while (nodo!=None) & (c<=pos):
                    aux=nodo
                    nodo=nodo.GetSiguiente()
                    c+=1
                return aux.GetDato()
            else:
                print("Fuera de los índices de la lista")
        else:
            print("Lista vacia")
            return None
        
    def EliminarNodo(self,pos):
        if not self.EstaVacia():
            if (pos <self.t) & (pos>=0):
                nodo=self.primero
                c=0
                if(pos==c):  
                    self.primero=self.primero.GetSiguiente()
                else:
                    while (nodo!=None) & (c<pos):
                        aux=nodo
                        nodo=nodo.GetSiguiente()
                        c+=1
                    aux.SetSiguiente(nodo.GetSiguiente())
                self.t=self.t-1
            if self.t==0:
                self.primero=None
            else:
                print("Fuera de los índices de la lista")
        else:
            print("Lista vacia")
            
    def ElDatosLista(self):
        self.primero=None
        self.t=0
        
    def Primero(self):
        return self.primero.GetDato()
    
    def Uiltimo(self):
        return self.ultimo.GetDato()
