from Sort import Sort
class Busqueda:
    def __init__(self, lista):
        self.lista=lista

    def BusquedaSecuencial(self, inicial):
        laux=[]
        for i in range(len(self.lista)):
          if self.lista[i][2][0]==inicial:
              laux=laux+[self.lista[i]]
        return laux
    
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
        l[i][2]=l[i][2]
    s=Sort()
    ordenado=s.BubbleSort(l)
    b=Busqueda(ordenado)
    while True:
        try:
            dato=input("""Ingrese dato de la siguiete form "A,1" """)
            dato=dato.split(",")
            letra=dato[0].upper()
            numero=int(dato[1])
            break
        except ValueError:
            print("Dato no valido")
    listaCompleta = []
    lista=b.BusquedaSecuencial(letra)
    for i in range(len(lista)):
        if int(lista[i][0]) >numero:
            listaCompleta.append(lista[i])
    print(listaCompleta)
    
if __name__=='__main__':
    main()