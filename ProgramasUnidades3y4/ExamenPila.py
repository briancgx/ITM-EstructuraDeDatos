import re

entrada = input("Por favor, ingresa una cadena: ")# Pedir al usuario una cadena en la misma línea y convertirla en una lista de caracteres
vector_caracteres = list(entrada)
operadores = []# Crear una lista para almacenar los operadores
operador_entre_paréntesis = re.findall(r'([+\-*/]) \(', entrada)# Crear una variable para rastrear el operador entre el primer y segundo paréntesis

for i, caracter in enumerate(vector_caracteres):# Encontrar todos los operadores dentro de los paréntesis
    if caracter == '(':
        j = i + 1
        while j < len(vector_caracteres) and vector_caracteres[j] != ')':
            if vector_caracteres[j] in "+-*/":
                operadores.append(vector_caracteres[j])
            j += 1     

numeros_como_cadenas = re.findall(r'\d+\.\d+|\d+', entrada) # Usar una expresión regular para encontrar todos los números como cadenas
numeros_como_floats = [float(numero) for numero in numeros_como_cadenas] # Convertir las cadenas de números en valores de punto flotante y almacenarlos en una lista
"""
# Imprimir el operador entre el primer y segundo paréntesis
if operador_entre_paréntesis is not None:
    print(f"Operador entre el primer y segundo paréntesis: {operador_entre_paréntesis[0]}")
else:
    print("No se encontró un operador entre el primer y segundo paréntesis.")

# Imprimir los otros operadores
for i, operador in enumerate(operadores):
    print(f"Operador del paréntesis {i + 1}: {operador}")

# Imprimir los números encontrados
print("Números encontrados:", numeros_como_floats)
"""
class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Crear los nodos para los números
numeros = [Nodo(numero) for numero in numeros_como_floats]

# Crear los nodos para los operadores
nodo_operador_entre_parentesis = Nodo(operador_entre_paréntesis[0])
nodo_operador_izquierda = Nodo(operadores[0])
nodo_operador_derecha = Nodo(operadores[1])

# Construir el árbol binario
nodo_operador_entre_parentesis.izquierda = nodo_operador_izquierda
nodo_operador_entre_parentesis.derecha = nodo_operador_derecha

nodo_operador_izquierda.izquierda = numeros[0]
nodo_operador_izquierda.derecha = numeros[1]

nodo_operador_derecha.izquierda = numeros[2]
nodo_operador_derecha.derecha = numeros[3]

# Función para evaluar el árbol
def evaluar(nodo):
    if nodo:
        if isinstance(nodo.valor, float):
            return nodo.valor
        izquierda = evaluar(nodo.izquierda)
        derecha = evaluar(nodo.derecha)
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            return izquierda / derecha

resultado = evaluar(nodo_operador_entre_parentesis) # Calcular el resultado
print("Resultado:", resultado) # Imprimir el resultado