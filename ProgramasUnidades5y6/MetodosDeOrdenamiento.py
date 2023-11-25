#La libreria csv se emplea para leer archivos separados por comas
import csv
#La clase Sort tiene los metodos de ordenamiento: Burbuja, QuickSort, ShellSort, y Radix
class Sort:
    "Metodo burbuja, itera en la lista para mover los datos de acuerdo al orden que se determine (ascendente o descendente)"
    def BubbleSortTraveler(self, lista):
        ordenado=False
        while not ordenado:
            ordenado=True #variable boleana para realizar el ordenamiento
            for i in range(len(lista)-1): #recorre desde la posicion 0 hasta el tamanio de la lista -2
                """Se determina el ordenamiento de los datos"""
                if lista[i][2]>lista[i+1][2]: #si el elemento de la lista actual es mayor que el siguiente, se realiza un cambio
                    aux=lista[i] #se almacena el elemento actual
                    lista[i]=lista[i+1] #el elemento siguiente se asigna a la posicion actual
                    lista[i+1]=aux #el elemento actual se asigna en la siguiente posición
                    ordenado=False #ya que se realizó el cambio, se asume que los elementos aun no están ordenados
        return lista #se devuelve el arreglo ordenado
    
    def BubbleSortDuration(self, lista):
        ordenado=False
        while not ordenado:
            ordenado=True #variable boleana para realizar el ordenamiento
            for i in range(len(lista)-1): #recorre desde la posicion 0 hasta el tamanio de la lista -2
                """Se determina el ordenamiento de los datos"""
                if lista[i][1]>lista[i+1][1]: #si el elemento de la lista actual es mayor que el siguiente, se realiza un cambio
                    aux=lista[i] #se almacena el elemento actual
                    lista[i]=lista[i+1] #el elemento siguiente se asigna a la posicion actual
                    lista[i+1]=aux #el elemento actual se asigna en la siguiente posición
                    ordenado=False #ya que se realizó el cambio, se asume que los elementos aun no están ordenados
        return lista #se devuelve el arreglo ordenado
    
    """El metodo SplitList() crea dos listas tomando en cuenta el primer elemento de la lista
    crea una lista cuyos datos sean menores que el pivote y una lista en el que los datos
    sean mayores o igual que el pivote"""
    def SplitList(self,lista):
        pivote=lista[0]
        listMenores=[]
        listMayores=[]
        #se recorre desde la posicion 1 hasta el tamanio de la lista-1
        for i in range (1,len(lista)):
            if(lista[i][2])<pivote[2]:
                listMenores.append(lista[i])
            else:
                listMayores.append(lista[i])
        #Se retornan los datos en el siguiente orden:
        return listMenores, pivote, listMayores
    
    def SplitListDuration(self,lista):
        pivote=lista[0]
        listMenores=[]
        listMayores=[]
        #se recorre desde la posicion 1 hasta el tamanio de la lista-1
        for i in range (1,len(lista)):
            if(lista[i][1])<pivote[1]:
                listMenores.append(lista[i])
            else:
                listMayores.append(lista[i])
        #Se retornan los datos en el siguiente orden:
        return listMenores, pivote, listMayores
    
    """El metodo QuickSort() es recursivo. Si la lista solo tiene un dato, se retorna ese mismo,
    de lo contrario se llama al metodo SplitList() para dividir la lista y luego rerornar la lista ordenada"""
    def QuickSortTraveler(self,lista): 
        if len(lista)<2: #si solo tiene un elemento o ninguno devuelve la lista
            return lista
        else: #si tiene mas de un elemento se procede a dividir la lista y ordenar recursivamente cada lista
            listMenores,pivote,listMayores=self.SplitList(lista)
            """Al retornar la lista se determina el orden de los datos:"""
            return self.QuickSortTraveler(listMenores)+[pivote]+self.QuickSortTraveler(listMayores)#al ordenar las listas se concatenan
    """El metodo de ordenamiento ShellSort() emplea iteraciones y un algoritmo de ordenación simple entre elementos que se encuentran a una distancia determinada
"""

    def QuickSortDuration(self,lista): 
        if len(lista)<2: #si solo tiene un elemento o ninguno devuelve la lista
            return lista
        else: #si tiene mas de un elemento se procede a dividir la lista y ordenar recursivamente cada lista
            listMenores,pivote,listMayores=self.SplitList(lista)
            """Al retornar la lista se determina el orden de los datos:"""
            return self.QuickSortDuration(listMenores)+[pivote]+self.QuickSortDuration(listMayores)#al ordenar las listas se concatenan


    def ShellSortTraveler (self, arreglo):
        tamanio=len(arreglo) #tamanio del arreglo
        intervalo=tamanio//2 #convierte el resultado a entero
        while intervalo>0: #mientras el intervalo sea mayor a 0 ingresa al ciclo
            #insert sort
            for i in range (intervalo, tamanio): #recorre desde intervalo hasta el tamanio del arreglo -1
                insertarValor=arreglo[i] #asignar el valor que se va a insertar
                insertarIndice=i #indice en el que se insertará el valor
                """si el valor de insertarIndice es mayor o igual que el intervalo y
                el valor de la posicion  (insertarIndice-intervalo) es mayor que el indice que el valor en
                el que se quiere insertar, entonces se hace el cambio.
                La comparacion establece el orden de la lista"""
                while insertarIndice<=intervalo and arreglo[insertarIndice-intervalo][2]>insertarValor[2]:
                    """En la posicion insertarIndice se asigna el dato de la posicion (insertarIndice-intervalo)"""
                    arreglo[insertarIndice]=arreglo[insertarIndice-intervalo]
                    """Se actualiza el valor de insertarIndice. insertarIndice=insertarIndice-intervalo"""
                    insertarIndice-=intervalo
                
                arreglo[insertarIndice]=insertarValor#se inserta el valor en el indice correspondiente
            intervalo=intervalo//2 #actualizar intervalo
        return arreglo
    
    
    def ShellSortDuration (self, arreglo):
        tamanio=len(arreglo) #tamanio del arreglo
        intervalo=tamanio//2 #convierte el resultado a entero
        while intervalo>0: #mientras el intervalo sea mayor a 0 ingresa al ciclo
            #insert sort
            for i in range (intervalo, tamanio): #recorre desde intervalo hasta el tamanio del arreglo -1
                insertarValor=arreglo[i] #asignar el valor que se va a insertar
                insertarIndice=i #indice en el que se insertará el valor
                """si el valor de insertarIndice es mayor o igual que el intervalo y
                el valor de la posicion  (insertarIndice-intervalo) es mayor que el indice que el valor en
                el que se quiere insertar, entonces se hace el cambio.
                La comparacion establece el orden de la lista"""
                while insertarIndice>=intervalo and arreglo[insertarIndice-intervalo][1]>insertarValor[1]:
                    """En la posicion insertarIndice se asigna el dato de la posicion (insertarIndice-intervalo)"""
                    arreglo[insertarIndice]=arreglo[insertarIndice-intervalo]
                    """Se actualiza el valor de insertarIndice. insertarIndice=insertarIndice-intervalo"""
                    insertarIndice-=intervalo
                
                arreglo[insertarIndice]=insertarValor#se inserta el valor en el indice correspondiente
            intervalo=intervalo//2 #actualizar intervalo
        return arreglo
    
    
    def RadixSort(self, lista):
        n = 0
        # Buscar la cantidad de dígitos en el número más grande de la segunda columna
        for e in lista:
            if len(str(e[1])) > n:
                n = len(str(e[1]))

        # Agregar ceros a la izquierda de los números que hagan falta
        for i in range(0, len(lista)):
            while len(str(lista[i][1])) < n:
                lista[i][1] = "0" + str(lista[i][1])

        for j in range(n - 1, -1, -1):
            # Almacenar en grupos en los que se almacenarán los números de acuerdo a la cantidad de dígitos
            grupos = [[] for i in range(10)]

            for m in range(len(lista)):
                # Grupo de la lista, y luego al dígito de la segunda columna
                digit = int(str(lista[m][1])[j]) if j > len(str(lista[m][1])) else 0
                grupos[digit].append(lista[m])

            lista = []  # Dejar la lista vacía
            for g in grupos:
                lista = g + lista

        for i in range(len(lista)):
            lista[i][1] = int(lista[i][1])

        return lista
    
    def MergeSortTraveler(self,lista):
    #tamaño de la lista
       if len(lista) < 2:
           return lista
    # De lo contrario, se divide en 2
       else:
           mitad = len(lista) // 2
           #print(lista[:mitad],"\n")
           izquierda = self.MergeSortTraveler(lista[:mitad])
           
           derecha = self.MergeSortTraveler(lista[mitad:])
           return self.MergeTraveler(derecha, izquierda)
       
    def MergeSortDuration(self,lista):
    #tamaño de la lista
       if len(lista) < 2:
           return lista
    # De lo contrario, se divide en 2
       else:
           mitad = len(lista) // 2
           #print(lista[:mitad],"\n")
           izquierda = self.MergeSortDuration(lista[:mitad])
           
           derecha = self.MergeSortDuration(lista[mitad:])
           return self.MergeDuration(derecha, izquierda)
       

    def Merge2Traveler(self,lista1, lista2):
        #print("Merge:")
        i, j = 0, 0 # Variables de incremento
        resultado = [] # Lista de resultado
 
   # Intercalar ordenadamente
        while(i < len(lista1) and j < len(lista2)):
            if (lista1[i][2] < lista2[j][2]):
                resultado.append(lista1[i])
                #print(lista1[i],"<",lista2[j])
                #print("r: ",resultado)
                i=i+1
            else:
                #print(i," ",j)
                #print(lista1[i],">=",lista2[j])
                resultado.append(lista2[j])
                #print("r: ",resultado)
                j=j+1
        #print("r: ",resultado)
 
   # Agregamos los resultados a la lista
        resultado=resultado+lista1[i:]
        #print("l1: ",lista1[i:])
        resultado=resultado+lista2[j:]
        #print("l2: ",lista2[j:])
        #print("r: ",resultado)
    # Retornamos el resultados
        return resultado
    
    def Merge2Duration(self,lista1, lista2):
        #print("Merge:")
        i, j = 0, 0 # Variables de incremento
        resultado = [] # Lista de resultado
 
   # Intercalar ordenadamente
        while(i < len(lista1) and j < len(lista2)):
            if (lista1[i][2] < lista2[j][2]):
                resultado.append(lista1[i])
                #print(lista1[i],"<",lista2[j])
                #print("r: ",resultado)
                i=i+1
            else:
                #print(i," ",j)
                #print(lista1[i],">=",lista2[j])
                resultado.append(lista2[j])
                #print("r: ",resultado)
                j=j+1
        #print("r: ",resultado)
 
   # Agregamos los resultados a la lista
        resultado=resultado+lista1[i:]
        #print("l1: ",lista1[i:])
        resultado=resultado+lista2[j:]
        #print("l2: ",lista2[j:])
        #print("r: ",resultado)
    # Retornamos el resultados
        return resultado
    
    def NaturalMerge2Traveler(self, lista):
        aux1 = []
        aux2 = []
        aux3 = []
        #mezcla = Sort()
        izquierda=0
        izq=0
        derecha = len(lista) - 1
        der = derecha
        ordenado = False
        #print(izquierda," |",derecha)
        while True:
            ordenado = True
            izquierda = 0
            #mientras la lista no este ordenada, se recorre
            #print("izquierda: ",izquierda,"derecha: ",derecha)
            while izquierda < derecha:
                #print("lactual: ",lista)
                #print(izquierda,"| ",derecha)
                izq = izquierda
                #recorre los elementos que están ordenados
                #recorre la lista
                while izq < derecha and lista[izq][2] <= lista[izq + 1][2]:
                    izq += 1
                #print(izquierda," ",izq+1)
                aux1 = lista[izquierda:izq+1]
                #print("aux1: ",aux1)
                der = izq + 1 #la siguiente posicion se asigna a der
                #comparar si el dato es menor al siguiente
                while der == derecha or der < derecha and lista[der][2] <= lista[der + 1][2]:
                    der += 1
                aux2 = lista[izq+1:der+1]#agrega los datos ordenados desde izq+1 hasta der+1
                #print("aux2: ",aux2)
                aux3 = lista[der+1:len(lista)]#agrega los ultimos datos a aux3
                #print("aux3: ",aux3)
                
                if len(aux3) > 0:
                    #si el ultimo elemento de aux2 es menor que el primero de aux3
                    if aux2[len(aux2) - 1][2] < aux3[0][1]:
                        aux2.extend(aux3)#agrega au3 a aux2
                        #print("aux2",aux2)
                        aux3.clear() #limpia aux3
                    else:
                    #si el ultimo elemento de aux2 es mayor o igual que el primero de aux3
                        #se agrega aux3 a aux1
                        aux1.extend(aux3)
                        #print("aux1",aux1)
                        aux3.clear()#limpia aux3
                #se llama al metodo Merge y se le pasan aux1 y aux2
                lista = self.Merge2Traveler(aux1, aux2)
                
                if len(aux2) == 0 and len(aux3) == 0:
                    ordenado = True
                    break
            if ordenado != False:
                break
        return lista
# Función merge


    def NaturalMerge2Duration(self, lista):
        aux1 = []
        aux2 = []
        aux3 = []
        #mezcla = Sort()
        izquierda=0
        izq=0
        derecha = len(lista) - 1
        der = derecha
        ordenado = False
        #print(izquierda," |",derecha)
        while True:
            ordenado = True
            izquierda = 0
            #mientras la lista no este ordenada, se recorre
            #print("izquierda: ",izquierda,"derecha: ",derecha)
            while izquierda < derecha:
                #print("lactual: ",lista)
                #print(izquierda,"| ",derecha)
                izq = izquierda
                #recorre los elementos que están ordenados
                #recorre la lista
                while izq < derecha and lista[izq][1] <= lista[izq + 1][1]:
                    izq += 1
                #print(izquierda," ",izq+1)
                aux1 = lista[izquierda:izq+1]
                #print("aux1: ",aux1)
                der = izq + 1 #la siguiente posicion se asigna a der
                #comparar si el dato es menor al siguiente
                while der == derecha or der < derecha and lista[der][1] <= lista[der + 1][1]:
                    der += 1
                aux2 = lista[izq+1:der+1]#agrega los datos ordenados desde izq+1 hasta der+1
                #print("aux2: ",aux2)
                aux3 = lista[der+1:len(lista)]#agrega los ultimos datos a aux3
                #print("aux3: ",aux3)
                
                if len(aux3) > 0:
                    #si el ultimo elemento de aux2 es menor que el primero de aux3
                    if aux2[len(aux2) - 1][2] < aux3[0][1]:
                        aux2.extend(aux3)#agrega au3 a aux2
                        #print("aux2",aux2)
                        aux3.clear() #limpia aux3
                    else:
                    #si el ultimo elemento de aux2 es mayor o igual que el primero de aux3
                        #se agrega aux3 a aux1
                        aux1.extend(aux3)
                        #print("aux1",aux1)
                        aux3.clear()#limpia aux3
                #se llama al metodo Merge y se le pasan aux1 y aux2
                lista = self.Merge2Duration(aux1, aux2)
                
                if len(aux2) == 0 and len(aux3) == 0:
                    ordenado = True
                    break
            if ordenado != False:
                break
        return lista

    def MergeTraveler(self,lista1, lista2):
        #print("Merge:")
        i, j = 0, 0 # Variables de incremento
        resultado = [] # Lista de resultado
 
   # Intercalar ordenadamente
        while(i < len(lista1) and j < len(lista2)):
            if (lista1[i][2] < lista2[j][2]):
                resultado.append(lista1[i])
                #print(lista1[i],"<",lista2[j])
                #print("r: ",resultado)
                i=i+1
            else:
                #print(i," ",j)
                #print(lista1[i],">=",lista2[j])
                resultado.append(lista2[j])
                #print("r: ",resultado)
                j=j+1
        #print("r: ",resultado)
 
   # Agregamos los resultados a la lista
        resultado=resultado+lista1[i:]
        #print("l1: ",lista1[i:])
        resultado=resultado+lista2[j:]
        #print("l2: ",lista2[j:])
        #print("r: ",resultado)
    # Retornamos el resultados
        return resultado
    
    def MergeDuration(self,lista1, lista2):
        #print("Merge:")
        i, j = 0, 0 # Variables de incremento
        resultado = [] # Lista de resultado
 
   # Intercalar ordenadamente
        while(i < len(lista1) and j < len(lista2)):
            if (lista1[i][1] < lista2[j][1]):
                resultado.append(lista1[i])
                #print(lista1[i],"<",lista2[j])
                #print("r: ",resultado)
                i=i+1
            else:
                #print(i," ",j)
                #print(lista1[i],">=",lista2[j])
                resultado.append(lista2[j])
                #print("r: ",resultado)
                j=j+1
        #print("r: ",resultado)
 
   # Agregamos los resultados a la lista
        resultado=resultado+lista1[i:]
        #print("l1: ",lista1[i:])
        resultado=resultado+lista2[j:]
        #print("l2: ",lista2[j:])
        #print("r: ",resultado)
    # Retornamos el resultados
        return resultado
    
    def NaturalMergeTraveler(self, lista):
        aux1 = []
        aux2 = []
        aux3 = []
        #mezcla = Sort()
        izquierda=0
        izq=0
        derecha = len(lista) - 1
        der = derecha
        ordenado = False
        #print(izquierda," |",derecha)
        while True:
            ordenado = True
            izquierda = 0
            #mientras la lista no este ordenada, se recorre
            #print("izquierda: ",izquierda,"derecha: ",derecha)
            while izquierda < derecha:
                #print("lactual: ",lista)
                #print(izquierda,"| ",derecha)
                izq = izquierda
                #recorre los elementos que están ordenados
                #recorre la lista
                while izq < derecha and lista[izq][2] <= lista[izq + 1][2]:
                    izq += 1
                #print(izquierda," ",izq+1)
                aux1 = lista[izquierda:izq+1]
                #print("aux1: ",aux1)
                der = izq + 1 #la siguiente posicion se asigna a der
                #comparar si el dato es menor al siguiente
                while der == derecha or der < derecha and lista[der][2] <= lista[der + 1][2]:
                    der += 1
                aux2 = lista[izq+1:der+1]#agrega los datos ordenados desde izq+1 hasta der+1
                #print("aux2: ",aux2)
                aux3 = lista[der+1:len(lista)]#agrega los ultimos datos a aux3
                #print("aux3: ",aux3)
                
                if len(aux3) > 0:
                    #si el ultimo elemento de aux2 es menor que el primero de aux3
                    if aux2[len(aux2) - 1][1] < aux3[0][2]:
                        aux2.extend(aux3)#agrega au3 a aux2
                        #print("aux2",aux2)
                        aux3.clear() #limpia aux3
                    else:
                    #si el ultimo elemento de aux2 es mayor o igual que el primero de aux3
                        #se agrega aux3 a aux1
                        aux1.extend(aux3)
                        #print("aux1",aux1)
                        aux3.clear()#limpia aux3
                #se llama al metodo Merge y se le pasan aux1 y aux2
                lista = self.MergeTraveler(aux1, aux2)
                
                if len(aux2) == 0 and len(aux3) == 0:
                    ordenado = True
                    break
            if ordenado != False:
                break
        return lista
    
    def NaturalMergeDuration(self, lista):
        aux1 = []
        aux2 = []
        aux3 = []
        #mezcla = Sort()
        izquierda=0
        izq=0
        derecha = len(lista) - 1
        der = derecha
        ordenado = False
        #print(izquierda," |",derecha)
        while True:
            ordenado = True
            izquierda = 0
            #mientras la lista no este ordenada, se recorre
            #print("izquierda: ",izquierda,"derecha: ",derecha)
            while izquierda < derecha:
                #print("lactual: ",lista)
                #print(izquierda,"| ",derecha)
                izq = izquierda
                #recorre los elementos que están ordenados
                #recorre la lista
                while izq < derecha and lista[izq][1] <= lista[izq + 1][1]:
                    izq += 1
                #print(izquierda," ",izq+1)
                aux1 = lista[izquierda:izq+1]
                #print("aux1: ",aux1)
                der = izq + 1 #la siguiente posicion se asigna a der
                #comparar si el dato es menor al siguiente
                while der == derecha or der < derecha and lista[der][1] <= lista[der + 1][1]:
                    der += 1
                aux2 = lista[izq+1:der+1]#agrega los datos ordenados desde izq+1 hasta der+1
                #print("aux2: ",aux2)
                aux3 = lista[der+1:len(lista)]#agrega los ultimos datos a aux3
                #print("aux3: ",aux3)
                
                if len(aux3) > 0:
                    #si el ultimo elemento de aux2 es menor que el primero de aux3
                    if aux2[len(aux2) - 1][1] < aux3[0][1]:
                        aux2.extend(aux3)#agrega au3 a aux2
                        #print("aux2",aux2)
                        aux3.clear() #limpia aux3
                    else:
                    #si el ultimo elemento de aux2 es mayor o igual que el primero de aux3
                        #se agrega aux3 a aux1
                        aux1.extend(aux3)
                        #print("aux1",aux1)
                        aux3.clear()#limpia aux3
                #se llama al metodo Merge y se le pasan aux1 y aux2
                lista = self.MergeDuration(aux1, aux2)
                
                if len(aux2) == 0 and len(aux3) == 0:
                    ordenado = True
                    break
            if ordenado != False:
                break
        return lista
    
    def OrdenarTraveler(self, lista):
        auxiliar=[]
        nlista=[]
        for i in range(0,len(lista)):
            if lista[i][2]==lista[i-1][2]:
                auxiliar.append(lista[i-1])
                if len(auxiliar)>1:
                    auxiliar.pop()
                auxiliar.append(lista[i])
            else:
                if len(auxiliar)>1:
                    auxiliar=self.NaturalMerge2Traveler(auxiliar)
                    for j in range(len(auxiliar)):
                        nlista.append(auxiliar[j])
                    auxiliar=[]
                nlista.append(lista[i])
        return nlista
    
    def OrdenarDuration(self, lista):
        auxiliar=[]
        nlista=[]
        for i in range(1,len(lista)):
            if lista[i][1]==lista[i-1][1]:
                auxiliar.append(lista[i-1])
                if len(auxiliar)>1:
                    auxiliar.pop()
                auxiliar.append(lista[i])
            else:
                if len(auxiliar)>1:
                    auxiliar=self.NaturalMerge2Duration(auxiliar)
                    for j in range(len(auxiliar)):
                        nlista.append(auxiliar[j])
                    auxiliar=[]
                nlista.append(lista[i])
        return nlista
    
    
def main():
    
    lista=[]
    with open ('Travel details dataset.csv') as file:
        reader = csv.reader(file)
        for fila in reader:
            lista.append([fila[1],fila[4],fila[5]])
    lista.pop(0)
    ordenamiento=Sort()
    for i in range(len(lista)):
        lista[i][2]=lista[i][2]
    BubbleSortTraveler=ordenamiento.BubbleSortTraveler(lista)
    mergeTraveler = ordenamiento.MergeTraveler([], lista)
    mergesortTraveler = ordenamiento.MergeSortTraveler(lista)
    NaturalMergeTraveler= ordenamiento.NaturalMergeTraveler(lista)
    OrdenarTraveler= ordenamiento.OrdenarTraveler(lista)
    QuickSortTraveler= ordenamiento.QuickSortTraveler(lista)
    ShellSortTraveler= ordenamiento.ShellSortTraveler(lista)
    SplitLisTraveler= ordenamiento.SplitList(lista)
    
    BubbleSortDuration=ordenamiento.BubbleSortDuration(lista)
    mergeDuration = ordenamiento.MergeDuration([], lista)
    mergesortDuration = ordenamiento.MergeSortDuration(lista)
    NaturalMergeDuration = ordenamiento.NaturalMergeDuration(lista)
    OrdenarDuration = ordenamiento.OrdenarDuration(lista)
    QuickSortDuration = ordenamiento.QuickSortDuration(lista)
    ShellSortDuration = ordenamiento.ShellSortDuration(lista)
    SplitLisDuration = ordenamiento.SplitList(lista)
    
    print("\nBubbleSort de la columna Traveler name (Mayor a Menor)")
    print(BubbleSortTraveler)
    print("\nMerge de la columna Traveler name (Mayor a Menor)")
    print(mergeTraveler)
    print("\nMergeSort de la columna Traveler name (Mayor a Menor)")
    print(mergesortTraveler)
    print("\nNaturalMerge de la columna Traveler name (Mayor a Menor)")
    print(NaturalMergeTraveler)
    print("\nOrdenar de la columna Traveler name (Mayor a Menor)")
    print(OrdenarTraveler)
    print("\nQuickSort de la columna Traveler name (Mayor a Menor)")
    print(QuickSortTraveler)
    print("\nShellSort de la columna Traveler name (Mayor a Menor)")
    print(ShellSortTraveler)
    print("\nSplitLis de la columna Traveler name (Mayor a Menor)")
    print(SplitLisTraveler)


    print("\nBubbleSort por medio de la columna Duration (Menor a Mayor)")
    print(BubbleSortDuration)
    print("\nMerge por medio de la columna Duration (Menor a Mayor)")
    print(mergeDuration)
    print("\nMergeSort por medio de la columna Duration (Menor a Mayor)")
    print(mergesortDuration)
    print("\nNaturalMerge por medio de la columna Duration (Menor a Mayor)")
    print(NaturalMergeDuration)
    print("\nOrdenar por medio de la columna Duration (Menor a Mayor)")
    print(OrdenarDuration)
    print("\nQuickSort por medio de la columna Duration (Menor a Mayor)")
    print(QuickSortDuration)
    print("\nShellSort por medio de la columna Duration (Menor a Mayor)")
    print(ShellSortDuration)
    print("\nSplitLis por medio de la columna Duration (Menor a Mayor)")
    print(SplitLisDuration)
   
if __name__=='__main__':
    main()