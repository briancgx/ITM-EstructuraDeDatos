class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
       
class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)
        self.c=""
    def agregar_hijos_izquierda(self, numero1,raiz1, numero2):
        self.raiz.izquierda=Nodo(raiz1)
        #self.raiz.derecha=Nodo(numero2)
        self.raiz.izquierda.izquierda=Nodo(numero1)
        self.raiz.izquierda.derecha=Nodo(numero2)
    def __agregar_recursivo(self, nodo, dato):
        if dato.GetNodo(0)< 18:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)
    def _agregar_izquierda_recursivo(self, nodo, dato):#se pasa la raiz y el dato
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._agregar_izquierda_recursivo(nodo.izquierda, dato)
                
    def _agregar_derecha_recursivo(self, nodo, dato):
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._agregar_derecha_recursivo(nodo.derecha, dato)        
    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            #print(nodo.dato.RecorrerInicio(), end=", ")
            #nodo.dato.RecorrerInicio()
            print(nodo.dato)
            self.c=self.c+str(nodo.dato)+" "
            #print(self.c)
    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
        
    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    def AgregarIzquierda(self, dato):
        self._agregar_izquierda_recursivo(self.raiz, dato)
    def AgregarDerecha(self, dato):
        self._agregar_derecha_recursivo(self.raiz, dato)
    def GetC(self):
        return self.c
cadena=input()
elementos=cadena.split(" ")
arbol=Arbol(elementos[5])
arbol.agregar_hijos_izquierda(elementos[1], elementos[2], elementos[3])
arbol.inorden()
arbol.postorden()
#print(arbol.GetC())
# n1=input("numero1")
# o=input("operador")
# n2=input("numero2")
# cadena=input("operacion")
# d=cadena.split()
# arbol = Arbol(d[1])
# arbol.agregar("María José")
# arbol.agregar("Maggie")
# arbol.agregar("Leon")
# arbol.agregar("Cuphead")
# arbol.agregar("Aloy")
# arbol.agregar("Jack")
# nombre = input("Ingresa algo para agregar al árbol: ")
# arbol.agregar(nombre)
# arbol.preorden()
# arbol.inorden()
# from calc import Calculadora
# arbol.AgregarIzquierda(d[0])
# arbol.AgregarDerecha(d[2])
# #arbol.AgregarIzquierda(3)
# arbol.postorden()
# print(arbol.GetC())
# calc=Calculadora(arbol.GetC())
# busqueda = input("Busca algo en el árbol: ")
# nodo = arbol.buscar(busqueda)
# if nodo is None:
#     print(f"{busqueda} no existe")
# else:
#     print(f"{busqueda} sí existe")
# from ListaDoblementeEnlazada import ListaDoblementeEnlazada
# a=ListaDoblementeEnlazada()
# a.AgregarUltimo(10)
# a.AgregarUltimo("josue")
# tree=Arbol(a)
# b=ListaDoblementeEnlazada()
# b.AgregarUltimo(20)
# b.AgregarUltimo("Emmanuel")
# tree.agregar(b)
# c=ListaDoblementeEnlazada()
# c.AgregarUltimo(4)
# c.AgregarUltimo("Martin")
# tree.agregar(c)
# tree.postorden()
