import csv

class OrdenadoRadix:

    def RadixSort(self, lista):
        n = 0
        for e in lista:
            if len(e) > n:
                n = len(e)
        for i in range(len(lista)):
            while len(lista[i]) < n:
                lista[i] += " "

        for j in range(n - 1, -1, -1):
            grupos = [[] for i in range(26)] 
            for m in range(len(lista)):
                grupos[ord(lista[m][j]) - ord('Z')].append(lista[m])
            lista = [] 
            for g in grupos:
                lista = lista + g
        return lista

lista = []

with open('Tokyo 2021 dataset v4.csv') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        lista.append(fila[7])
    lista.pop(0) 

ordenador = OrdenadoRadix()
lista_ordenada = ordenador.RadixSort(lista)

print(lista_ordenada)
