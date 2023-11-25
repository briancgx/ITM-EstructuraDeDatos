class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None
    def GetDato(self):
        return self.dato
    def GetSiguiente(self):
        return self.siguiente
    def SetDato(self,nuevoDato):
        self.dato=nuevoDato
    def SetSiguiente(self,nuevoSig):
        self.siguiente=nuevoSig
    def GetAnterior(self):
        return self.anterior
    def SetAnterior(self,nuevoAnt):
        self.anterior=nuevoAnt
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.t=0
    def EstaVacia(self):
        return self.primero==None
    def AgregarUltimo(self,dato):
        if self.EstaVacia():
            self.ultimo=Nodo(dato)
            self.primero=self.ultimo
        else:
            aux=self.ultimo
            nnodo=Nodo(dato)
            #print("dato: ",self.ultimo.GetDato())
            aux.SetSiguiente(nnodo)
           # self.ultimo.SetAnterior(aux)
            self.ultimo=nnodo
            self.ultimo.SetAnterior(aux)
        self.t+=1
    def AgregarInicio(self,dato):
        if self.EstaVacia():
            self.ultimo=Nodo(dato)
            self.primero=self.ultimo
        else:
            aux=Nodo(dato)
            aux.SetSiguiente(self.primero)
            self.primero.SetAnterior(aux)
            self.primero=aux
        self.t+=1

    def RecorrerInicio(self):
        if not self.EstaVacia():
            nodo=self.primero
            datos="["
            while nodo!=None:
                #print(nodo.GetDato())
                if(nodo.GetSiguiente()!=None):
                    datos=datos+str(nodo.GetDato())+","
                    nodo=nodo.GetSiguiente()
                else:
                    datos=datos+str(nodo.GetDato())+"]"
                    nodo=nodo.GetSiguiente()
                    #print(nodo)
            print(datos)
        else:
            print("Lista vacia")
    def RecorrerFinal(self):
        if not self.EstaVacia():
            nodo=self.ultimo
            datos="["
            while nodo!=None:
                if(nodo.GetAnterior()!=None):
                    datos=datos+str(nodo.GetDato())+","
                    nodo=nodo.GetAnterior()
                else:
                    datos=datos+str(nodo.GetDato())+"]"
                    nodo=nodo.GetAnterior()
            print(datos)
        else:
            print("Lista vacia")
    def Tamanio(self):
        return self.t
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
            else:
                print("Fuera de los índices de la lista")
            if self.t==0:
                self.primero=None
                self.ultimo=None
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
                else:
                    anterior.SetSiguiente(nodo.GetSiguiente())
                self.t=self.t-1
            if self.t==0:
                self.primero=None
                self.ultimo=None
        else:
            print("lista vacia")
    def ElDatosLista(self):
        self.primero=None
        self.ultimo=None
        self.t=0
    def Insertar(self, pos,dato):
        if not self.EstaVacia():
        
            if pos==0:

            # self.ultimo=Nodo(dato)
            # self.ultimo.SetSiguiente(self.primero)
            # self.primero=self.ultimo
                aux=Nodo(dato)
                aux.SetSiguiente(self.primero)
                self.primero.SetAnterior(aux)
                self.primero=aux
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
                    nnodo.SetAnterior(aux)
                    nnodo.SetSiguiente(nodo)
                    nodo.SetAnterior(nnodo)
                    self.t=self.t+1
                else:
                    print("Fuera de los índices de la lista")
            
        else:
            print("Lista vacia")

    def SetNodo(self,pos,dato):
        if not self.EstaVacia():
            nodo=self.primero
            if(pos <self.t) & (pos>=0):
                c=0
                while (nodo!=None) & (c<=pos):
                    aux=nodo
                    nodo=nodo.GetSiguiente()
                    c+=1
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
                    #print(c)
                    aux=nodo
                    nodo=nodo.GetSiguiente()
                    c+=1
                return aux.GetDato()
            else:
                print("Fuera de los índices de la lista")
        else:
            print("Lista vacia")
            return None
    def GetPrimero(self):
        if not self.EstaVacia():
            return self.primero.GetDato()
        print("Lista Vacia")
        return None
    def GetUiltimo(self):
        if not self.EstaVacia():
            return self.ultimo.GetDato()
        print("Lista Vacia")
        return None