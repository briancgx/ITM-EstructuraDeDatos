class SumaVectores:
    def __init__(self, cadena):
        self.vectores = self.divisionCadena(cadena)
        self.sumas = [self.sumaElementos(vector) for vector in self.vectores]

    def divisionCadena(self, cadena):
        vectores = cadena.split(';')
        vectores = [vector.split(',') for vector in vectores]
        return vectores

    def sumaElementos(self, vector):
        if not vector:
            return 0
        else:
            return int(vector[0]) + self.sumaElementos(vector[1:])

def main():
    entrada = input("Ingresar vectores separados por ';' y los elementos de cada uno separados por ',' (Ejemplo: 1,2,3;0,2,2,3 ): ")
    sumaVectores = SumaVectores(entrada)
    sumaTotal = sum(sumaVectores.sumas)
    print("La suma total es:", sumaTotal)

if __name__ == '__main__':
    main()
    
# Brian Azael Cumi Guzman
