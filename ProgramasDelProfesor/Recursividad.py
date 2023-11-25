class recursiva:
    def __init__(self, n, m):
       self.n=n
       self.m=m
       self.diccionario={0:1}
       if self.n>self.m:
           factn=self.factRecursivo(self.n)
           factm=self.diccionario[self.m]
           resultado=factn+factm
           print(resultado)
       else:
           factm=self.factRecursivo(self.m)
           factn=self.diccionario[self.n]
           resultado=factn+factm
           print(resultado)           
       
    def factRecursivo(self, num):
        
        if num==0:
            return 1
        else:
            fact=num*self.factRecursivo(num-1)
            self.diccionario[num]=fact
            return fact
    
    
entrada=input()
print(entrada)
dividida=entrada.split(",")
print(dividida)
for i in range(len(dividida)):
    dividida[i]=int(dividida[i])
    print(dividida[i])

r=recursiva(dividida[0],dividida[1])