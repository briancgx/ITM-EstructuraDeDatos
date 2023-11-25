class Replicador:
    def __init__(self):
        self.vector = ""
        self.n = 0

    def replicar(self, vector, n):
        elementos = vector.split(',')
        resultado = []

        for elemento in elementos:
            elemento = int(elemento)
            resultado.extend([elemento] * n)

        return resultado

    def entrada(self):
        entrada = input("Ingrese el vector y el valor de n. Por ejemplo: (1,2,3,4;2): ")
        self.vector, n_str = entrada.split(';')
        self.n = int(n_str)

    def ejecutar(self):
        nuevo_vector = self.replicar(self.vector, self.n)
        resultado_str = ','.join(map(str, nuevo_vector))
        print(resultado_str)

if __name__ == "__main__":
    replicador = Replicador()
    replicador.entrada()
    replicador.ejecutar()

# Brian Azael Cumi Guzman