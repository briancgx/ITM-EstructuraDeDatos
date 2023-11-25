class Pila(list):
    def Push(self, item):
        self.append(item)

    def Pop(self):
        if not self.isEmpty():
            return self.pop()
        else:
            return None

    def isEmpty(self):
        return len(self) == 0

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def es_operador(char):
    operadores = "+-*/%"
    return char in operadores

def aplicar_operador(operador, operando1, operando2):
    if operador == "+":
        return operando1 + operando2
    elif operador == "-":
        return operando1 - operando2
    elif operador == "*":
        return operando1 * operando2
    elif operador == "/":
        return operando1 / operando2
    elif operador == "%":
        return operando1 % operando2

def construir_arbol(expresion):
    pila = Pila()
    lista_expresion = expresion.split()
    for char in lista_expresion:
        if char == ")":
            subarbol = []
            while pila[-1] != "(":
                subarbol.insert(0, pila.Pop())
            pila.Pop()  # Pop the '('
            for elemento in subarbol:
                if isinstance(elemento, Nodo) and es_operador(elemento.valor):
                    nodo = elemento
                    nodo.derecha = pila.Pop()
                    nodo.izquierda = pila.Pop()
                    pila.Push(nodo)
                else:
                    pila.Push(elemento)
        elif char == "(":
            pila.Push(char)
        else:
            # Elimina los paréntesis y maneja números
            char = char.replace("(", "").replace(")", "")
            if not es_operador(char):
                pila.Push(Nodo(float(char)))
            else:
                pila.Push(char)

    return pila[0]

def evaluar_arbol(arbol):
    if isinstance(arbol, Nodo):
        if arbol.valor in ('+', '-', '*', '/', '%'):
            izquierda = evaluar_arbol(arbol.izquierda)
            derecha = evaluar_arbol(arbol.derecha)
            resultado = aplicar_operador(arbol.valor, izquierda, derecha)
            return resultado
        return float(arbol.valor)  # Convert leaf values to a numeric type
    return float(arbol)  # Convert leaf values to a numeric type


# Código en notación inorden
def construir_arbol_inorden(expresion):
    operadores = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    pila_operadores = []
    pila_operandos = []
    elementos = expresion.split()

    def aplicar_operador(operador):
        operando2, operando1 = pila_operandos.pop(), pila_operandos.pop()
        nodo = Nodo(operador)
        nodo.izquierda, nodo.derecha = operando1, operando2
        pila_operandos.append(nodo)

    for elemento in elementos:
        if elemento in '+-*/%':
            while (pila_operadores and pila_operadores[-1] in operadores and
                   operadores[elemento] <= operadores[pila_operadores[-1]]):
                aplicar_operador(pila_operadores.pop())
            pila_operadores.append(elemento)
        elif elemento == '(':
            pila_operadores.append(elemento)
        elif elemento == ')':
            while pila_operadores[-1] != '(':
                aplicar_operador(pila_operadores.pop())
            pila_operadores.pop()
        else:
            pila_operandos.append(Nodo(float(elemento)))

    while pila_operadores:
        aplicar_operador(pila_operadores.pop())

    return pila_operandos[0]

def evaluar_arbol(arbol):
    if arbol.valor in ('+', '-', '*', '/', '%'):
        izquierda, derecha = evaluar_arbol(arbol.izquierda), evaluar_arbol(arbol.derecha)
        resultado = aplicar_operador(arbol.valor, izquierda, derecha)
        return resultado
    return arbol.valor

expresion_inorden = input("Ingresa la expresión en notación inorden: ")
arbol_inorden = construir_arbol_inorden(expresion_inorden)
try:
    resultado_inorden = evaluar_arbol(arbol_inorden)
    print("Resultado en notación inorden:", resultado_inorden)
except ValueError as e:
    print(e)
