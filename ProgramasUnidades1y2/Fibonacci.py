class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.diccionario = {0:1, 1:1}
        print(self.fibonacci(self.n))
        
    def fibonacci(self, fib):
        if fib in self.diccionario:
            return self.diccionario[fib]
        else:
            a = self.fibonacci(fib-1)
            b = self.fibonacci(fib-2)
            c = a + b
            return c
def main():
    numero = int(input())
    f = Fibonacci(numero)
if __name__ == '__main__':
    main()