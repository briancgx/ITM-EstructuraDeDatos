class NodoExpresion:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def construir_arbol_inorden(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    pila_operadores = []
    pila_operandos = []
    elementos = expresion.split()

    for elemento in elementos:
        if elemento in '+-*/%':
            while (pila_operadores and pila_operadores[-1] in precedencia and
                   precedencia[elemento] <= precedencia[pila_operadores[-1]]):
                operador = pila_operadores.pop()
                operando2, operando1 = pila_operandos.pop(), pila_operandos.pop()
                nodo = NodoExpresion(operador)
                nodo.izquierda, nodo.derecha = operando1, operando2
                pila_operandos.append(nodo)
            pila_operadores.append(elemento)
        elif elemento == '(':
            pila_operadores.append(elemento)
        elif elemento == ')':
            while pila_operadores[-1] != '(':
                operador = pila_operadores.pop()
                operando2, operando1 = pila_operandos.pop(), pila_operandos.pop()
                nodo = NodoExpresion(operador)
                nodo.izquierda, nodo.derecha = operando1, operando2
                pila_operandos.append(nodo)
            pila_operadores.pop()
        else:
            pila_operandos.append(NodoExpresion(float(elemento)))

    while pila_operadores:
        operador = pila_operadores.pop()
        operando2, operando1 = pila_operandos.pop(), pila_operandos.pop()
        nodo = NodoExpresion(operador)
        nodo.izquierda, nodo.derecha = operando1, operando2
        pila_operandos.append(nodo)

    return pila_operandos[0]

def evaluar_arbol(arbol):
    if arbol.valor in '+-*/%':
        izquierda, derecha = evaluar_arbol(arbol.izquierda), evaluar_arbol(arbol.derecha)
        if arbol.valor == '+':
            return izquierda + derecha
        elif arbol.valor == '-':
            return izquierda - derecha
        elif arbol.valor == '*':
            return izquierda * derecha
        elif arbol.valor == '/':
            if derecha == 0:
                raise ValueError("No es posible dividir entre cero")
            return izquierda / derecha
        elif arbol.valor == '%':
            if derecha == 0:
                raise ValueError("No es posible obtener el residuo de la división entre cero")
            return izquierda % derecha
    return arbol.valor

expresion = input("Ingresa la expresión en notación inorden: ")
arbol = construir_arbol_inorden(expresion)
try:
    resultado = evaluar_arbol(arbol)
    print("Resultado de la expresión:", resultado)
except ValueError as e:
    print("La expresión no es válida:", e)
    
# Brian Azael Cumi Guzman