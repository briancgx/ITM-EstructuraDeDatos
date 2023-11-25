from Pila import Pila
error=False
dis=input("HP-35\n")
datos=dis.split() # Se divide la cadena por espacios en blanco
p=Pila() 
for i in range(len(datos)): # Recorre los elementos de la lista
    #print(datos[i]) 
    try: # Bloque que podría producir una excepción
        n=float(datos[i]) # Intenta convertir el caracter en un dato float
        p.Push(n) # Si lo convirtió lo agrega a la pila
    except ValueError:   # Bloque para manejar la excepción 
        if datos[i] not in "+-/*%": #si el caracter no es algún operando se lanza la excepción 
            raise ValueError("Operando inválido")
        try: # Si el caracter es un operador, se proceden a recuperar los dos operandos para realizar
            # Se realiza el cálculo
                n1 = p.Pop()
                n2 = p.Pop()
                #print(n1," ",n2)
                if datos[i]=="+":
                    c=n1+n2
                elif datos[i]=="-":
                    c=n2-n1
                elif datos[i]=="*":
                    c=n2*n1
                elif datos[i]=="/":
                    try:
                        c = n2 / n1
                    except ZeroDivisionError:
                        c = "No es posible dividir entre cero"
                elif datos[i]=="%":
                    try:
                        c = n2 % n1
                    except ZeroDivisionError:
                        c = "No es posible obtener el residuo de la división entre cero"
                                    
                p.Push(c) # Se apila el resultado de la operación

        except TypeError: # Si no se pudo realizar la suma entonces faltaban números
            print("Faltan operandos")

            error=True # Se asigna True a la variable error
 
if p.tamanio()>1: # Si hay más de un número en la pila entonces hizo falta operadores
    error=True
    print("Faltan operadores")

if(not error):
    print("resultado: ",p.Pop())