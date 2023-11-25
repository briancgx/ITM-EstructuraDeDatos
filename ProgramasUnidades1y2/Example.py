class Persona:
    def __init__(self, edad, nacionalidad, genero):
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.genero = genero

    def imprimir(self):
        print("Edad: ", self.edad, " ", "Nacionalidad", self.nacionalidad, " ", "Genero", self.genero)
        
    def validar(self, n):
        a=3*n
        cumple = True#False
        while(cumple):
            if a<10:
                cumple = True
                nuevo=int(input())
                n=nuevo
                a=3*n
            else:
                cumple = False                       

    def uso_de_for(self):
        for i in range(0, 10):
            print(i)

p = Persona(edad=" ", nacionalidad=" ", genero=" ")
p.uso_de_for()

"""
error=True
while error==True:  
    try:
        ed=int(input())
        error=False
    except ValueError:
        print("Ingresa un numero")
        error=True
"""
    
# ed=input()
# na=input()
# ge=input()
# p = Persona(edad=ed, nacionalidad=na, genero=ge)
# p.imprimir()

# p.validar(int(input()))