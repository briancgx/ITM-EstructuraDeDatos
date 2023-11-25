from Sort import Sort
class Busqueda:
    def __init__(self, lista):
        self.lista=lista

    def BusquedaSecuencial(self, inicial):
        laux=[]
        for i in range(len(self.lista)):
          if self.lista[i][1][0]==inicial:
              laux=laux+[self.lista[i]]
        return laux
    
    def BusquedaBinaria(self, dato):
        tamanio=len(self.lista)
        #print("t: ",tamanio)
        cont=0
        inferior=0
        superior=tamanio
        
        while (inferior<=superior) and (cont<tamanio):
            mitad=(inferior+superior)//2
            if self.lista[mitad][0]==dato:
                return self.lista[mitad]
            elif self.lista[mitad][0]>dato:
                    superior=mitad
            elif self.lista[mitad][0]<dato:
                    inferior=mitad
            cont=cont+1
        return False
def main():
    import csv
    l=[]
    with open('Tokyo 2021 dataset v4.csv') as File:
         reader = csv.reader(File)
         for row in reader:
             l.append([row[5],row[7],row[8]])
        
    #print("lista=",l)
    l.pop(0)
    for i in range(len(l)):
        l[i][0]=int(l[i][0])
    s=Sort()
    ordenado=s.BubbleSort(l)
    b=Busqueda(ordenado)
    dato=input()

    print(b.BusquedaSecuencial(dato))
    
if __name__=='__main__':
    main()