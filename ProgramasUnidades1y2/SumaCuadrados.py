class SumaCuadrados:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.operaciones = {}

    def suma(self, n):
        if n == 0:
            return 0
            return 0
        else :
            cuadrado = n ** 2
            sumaDiccionario = cuadrado + self.suma(n-1)
            self.operaciones[n] = sumaDiccionario
            return cuadrado + self.suma(n-1)
        
def main():
    entrada = input("Ingrese dos numeros separados por coma(Ejemplo: 4,2): ")
    a, b = map(int, entrada.split(","))
    calculoSumaCuadrados = SumaCuadrados(a, b)
    
    resultado_1 = calculoSumaCuadrados.suma(b)
    resultado_2 = calculoSumaCuadrados.suma(a)
    print("{},{}".format(resultado_2, resultado_1))
        
if __name__ == '__main__':
    main()
    
# Brian Azael Cumi Guzman 3SA
        