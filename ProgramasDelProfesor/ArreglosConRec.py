class arreglosRec:
    def __init__(self, n, m):
        self.mat=[]
        for i in range(n):
            self.mat.append([])
            for j in range(m):
                self.mat[i].append(0)
    def getMat(self):
        return self.mat
        
    def recorrerColumnas(self, mat, inFila, inColumna):
        if inColumna<len(mat[inFila]):
            print(mat[inFila][inColumna])
            self.recorrerColumnas(mat, inFila, inColumna+1)
        
        
    def recorrerFilas(self, mat, inFila):
        if inFila<len(mat):
            self.recorrerColumnas(mat, inFila, 0)
            self.recorrerFilas(mat, inFila+1)
            
            
            
        
def main():
    datos=input().split(",")
    l=[]
    for i in range(len(datos)):
        l.append(int(datos[i]))
    objeto=arreglosRec(l[0], l[1])
    matriz=objeto.getMat()
    objeto.recorrerFilas(matriz, 0)
if __name__=='__main__':
    main()