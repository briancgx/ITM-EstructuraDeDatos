from Pila import Pila
error=False
dis=input("HP-35\n")
datos=dis.split() #se divide la cadena por espacios en blanco
p=Pila() #
for i in range(len(datos)): #recorre los elementos de la lista
    #print(datos[i]) 
    try: #bloque que podría producir una excepción
        n=float(datos[i]) #intenta convertir el caracter en un dato float
        p.Push(n) #si lo convirtió lo agrega a la pila
    except ValueError:   #bloque para manejar la excepción 
        if datos[i] not in "+-/*%": #si el caracter no es algún operando se lanza la excepción 

            raise ValueError("Operando inválido")
        try: # si el caracter es un operador, se proceden a recuperar los dos operandos para realizar
            #el cálculo
                n1 = p.Pop()
                n2 = p.Pop()
                #print(n1," ",n2)
                if datos[i]=="+":
                    c=n1+n2

                p.Push(c) #se apila el resultado de la operación

        except TypeError: #si no se pudo realizar la suma entonces faltaban números
            print("Faltan operandos")

            error=True #se asigna True a la variable error
 
if p.tamanio()>1: #si hay más de un número en la pila entonces hizo falta operadores
    error=True
    print("Faltan operadores")

if(not error):
    print("resultado: ",p.Pop())