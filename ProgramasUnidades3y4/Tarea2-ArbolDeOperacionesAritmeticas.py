class Tarea2:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def evaluar_arbol(nodo):
    if nodo.valor.isnumeric():
        return int(nodo.valor)
    else:
        izquierda = evaluar_arbol(nodo.izquierda)
        derecha = evaluar_arbol(nodo.derecha)
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            if derecha == 0:
                raise ZeroDivisionError("División por cero")
            return izquierda / derecha

def construir_arbol(expresion):
    operadores = {'+', '-', '*', '/'}
    prioridad = {'+': 1, '-': 1, '*': 2, '/': 2}

    def es_operador(token):
        return token in operadores

    def es_menor_precedencia(op1, op2):
        return prioridad[op1] <= prioridad[op2]

    def convertir_a_postfija(expresion):
        pila_operadores = []
        postfija = []

        tokens = expresion.split()
        for token in tokens:
            if token == "(":
                pila_operadores.append(token)
            elif token == ")":
                while pila_operadores and pila_operadores[-1] != "(":
                    postfija.append(pila_operadores.pop())
                pila_operadores.pop()
            elif es_operador(token):
                while (pila_operadores and es_operador(pila_operadores[-1]) and
                       es_menor_precedencia(pila_operadores[-1], token)):
                    postfija.append(pila_operadores.pop())
                pila_operadores.append(token)
            else:
                postfija.append(token)

        while pila_operadores:
            postfija.append(pila_operadores.pop())

        return postfija

    def construir_arbol_postfija(postfija_tokens):
        pila_nodos = []

        for token in postfija_tokens:
            if not es_operador(token):
                pila_nodos.append(Tarea2(token))
            else:
                nodo_derecha = pila_nodos.pop()
                nodo_izquierda = pila_nodos.pop()
                nodo = Tarea2(token)
                nodo.izquierda = nodo_izquierda
                nodo.derecha = nodo_derecha
                pila_nodos.append(nodo)

        return pila_nodos[0]

    postfija_expresion = convertir_a_postfija(expresion)
    arbol = construir_arbol_postfija(postfija_expresion)

    return arbol

def recorrido_preorden(nodo):
    if nodo:
        print(nodo.valor, end=' ')
        recorrido_preorden(nodo.izquierda)
        recorrido_preorden(nodo.derecha)

def recorrido_inorden(nodo):
    if nodo:
        recorrido_inorden(nodo.izquierda)
        print(nodo.valor, end=' ')
        recorrido_inorden(nodo.derecha)

def recorrido_posorden(nodo):
    if nodo:
        recorrido_posorden(nodo.izquierda)
        recorrido_posorden(nodo.derecha)
        print(nodo.valor, end=' ')

expresion = input("Ingresa una expresión aritmética: ")
arbol = construir_arbol(expresion)

print("Recorrido Preorden:")
recorrido_preorden(arbol)
print("\nRecorrido Inorden:")
recorrido_inorden(arbol)
print("\nRecorrido Posorden:")
recorrido_posorden(arbol)

try:
    resultado = evaluar_arbol(arbol)
    print("\nResultado de la expresión:", resultado)
except ZeroDivisionError as e:
    print("Error:", e)
    
# Brian Azael Cumi Guzmán