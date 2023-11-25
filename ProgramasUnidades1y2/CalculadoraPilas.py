class Calculadora:
    def __init__(self):
        self.pila = [] 

    def calcular(self, expresion):
        try:
            operadores = {'+', '-', '*', '/'}
            tokens = expresion.split()
            
            for token in tokens:
                if token not in operadores:
                    self.pila.append(float(token))
                else:
                    if len(self.pila) < 2:
                        return "Error: Faltan operandos"
                    
                    operando2 = self.pila.pop()  
                    operando1 = self.pila.pop()  
                    
                    if token == '+':
                        resultado = operando1 + operando2
                    elif token == '-':
                        resultado = operando1 - operando2
                    elif token == '*':
                        resultado = operando1 * operando2
                    elif token == '/':
                        if operando2 == 0:
                            return "Error: División por cero"
                        resultado = operando1 / operando2
                    
                    self.pila.append(resultado) 
            
            if len(self.pila) == 1:
                return self.pila[0]  
            else:
                return "Error: Expresión no válida" 
        
        except ValueError:
            return "Entrada no válida. Debe ser en formato de notación posfija."
# Brian Azael Cumi Guzman 3SA