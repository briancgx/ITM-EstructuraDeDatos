from SortMDB import SortMDB

class Busqueda:
    def __init__(self, lista):
        self.lista = lista
        self.tabla_hash = self.crear_tabla_hash()

    def crear_tabla_hash(self):
        return {elemento[0]: elemento for elemento in self.lista}

    def BusquedaSecuencial(self, inicial):
        laux = []
        for i in range(len(self.lista)):
            if self.lista[i][0] == inicial:
                laux.append(self.lista[i])
        return laux

    def BusquedaBinaria(self, dato):
        tamanio = len(self.lista)
        cont = 0
        inferior = 0
        superior = tamanio - 1 

        while inferior <= superior and cont < tamanio:
            mitad = (inferior + superior) // 2
            if self.lista[mitad][0] == dato:
                return [self.lista[mitad]]
            elif self.lista[mitad][0] > dato:
                superior = mitad - 1
            else:
                inferior = mitad + 1
            cont += 1

        return []


    def BusquedaHash(self, dato):
        if dato in self.tabla_hash:
            return [self.tabla_hash[dato]]
        else:
            return []


def main():
    import csv

    l = []
    with open('Tokyo 2021 dataset v4.csv') as File:
        reader = csv.reader(File)
        for row in reader:
            l.append([row[5], row[7], row[8]])

    l.pop(0)
    for i in range(len(l)):
        l[i][0] = int(l[i][0])

    s = SortMDB()
    ordenado = s.QuickSort(l)
    b = Busqueda(ordenado)

    dato = int(input("Ingrese el valor a buscar: "))

    resultados_secuencial = b.BusquedaSecuencial(dato)
    resultados_binaria = b.BusquedaBinaria(dato)
    resultados_hash = b.BusquedaHash(dato)

    print("\nBúsqueda secuencial:")
    if resultados_secuencial:
        for resultado in resultados_secuencial:
            print(resultado)
    else:
        print("No se encontraron coincidencias en la búsqueda secuencial.")

    print("\nBúsqueda binaria:")
    if resultados_binaria:
        for resultado in resultados_binaria:
            print(resultado)
    else:
        print("No se encontraron coincidencias en la búsqueda binaria.")

    print("\nBúsqueda en tabla hash:")
    if resultados_hash:
        for resultado in resultados_hash:
            print(resultado)
    else:
        print("No se encontraron coincidencias en la búsqueda en tabla hash.")

if __name__ == '__main__':
    main()
