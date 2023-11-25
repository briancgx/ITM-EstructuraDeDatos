import csv

class Sort:
    def OrdenDescendente(self, arreglo):
        longArrgeglo = len(arreglo)
        intervalo = longArrgeglo // 2

        while intervalo > 0:
            for i in range(intervalo, longArrgeglo):
                valor = arreglo[i]
                indice = i

                while indice >= intervalo and arreglo[indice - intervalo][2][0] < valor[2][0]:
                    arreglo[indice] = arreglo[indice - intervalo]
                    indice -= intervalo

                arreglo[indice] = valor

            intervalo = intervalo // 2

        return arreglo

def main():
    lista = []

    with open('Tokyo 2021 dataset v4.csv') as file:
        reader = csv.reader(file)
        for fila in reader:
            lista.append([fila[7], fila[5], fila[8]])

    lista.pop(0)

    ordenamiento = Sort()

    for i in range(len(lista)):
        lista[i][1] = int(lista[i][1])

    input_str = input("Ingrese una cadena en el formato letra_mayuscula1,letra_mayuscula2: ")

    letras = input_str.split(',')

    if letras[0] <= letras[1]:
        Shell_descending = ordenamiento.OrdenDescendente(lista)
        result_matrix = [row for row in Shell_descending if letras[0] <= row[0][0] <= letras[1]]
        print(result_matrix)
    else:
        print([])

if __name__ == '__main__':
    main()
