inp=input().split(',')
inp[0]=int(inp[0])
inp[1]=int(inp[1])
sumados={}

def sumar_primeros(numero):
    if numero==0:
        sumados[numero]=numero
        return numero
    else:
        suma=numero*numero+sumar_primeros(numero-1)
        sumados[numero]=suma
        return suma

if inp[0]>inp[1]:
    suma1=sumar_primeros(inp[0])
    suma2=sumados[inp[1]]
    print(suma1,',', suma2)

else:
    suma2=sumar_primeros(inp[1])
    suma1=sumados[inp[0]]
    print(suma1,',', suma2)