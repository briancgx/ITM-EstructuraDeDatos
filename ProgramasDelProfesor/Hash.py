class hash_table:
    def __init__(self):
        self.table = [None] * 93
        #print(self.table)
    # Función hash
    def tabblaActual(self):
        return self.table
    def Hash_func(self, value):
        key = 0
        for i in range(len(value[0])):
            #print(value[0][i])
            key += ord(value[0][i])
        for j in range(len(value[1])):
            key += ord(value[1][j])
        return key%93
    def Insert(self, value): # Metodo para ingresar elementos
        numeroHash = self.Hash_func(value)
        #print(hash)
        if self.table[numeroHash] == None:
            self.table[numeroHash] = value

    def Search(self,value): # Metodo para buscar elementos
        numeroHash = self.Hash_func(value);
        if self.table[numeroHash]!=None:
            return self.table[numeroHash]
        else:
            return False
  
    def Remove(self,value): # Metodo para eleminar elementos
        numeroHash = self.Hash_func(value);
        if self.table[numeroHash] == None:
            print("No hay elementos con ese valor", value)
        else:
            print("Elemento con valor", value, "eliminado")
            self.table[numeroHash] = None;

def main():
    import csv
    l=[]
    with open('Tokyo 2021 dataset v4.csv') as File:
         reader = csv.reader(File)
         for row in reader:
             l.append([row[5],row[7]])
    l.pop(0)
    # print(len(l))
    # print(len(l[0]))

    # for i in range(len(l)):
    #     l[i][0]=int(l[i][0])
    ht=hash_table()
    for i in range(len(l)):
        ht.Insert(l[i])
    print(ht.tabblaActual())
    print("esta 133?",ht.Search(["113",'USA']))
if __name__=='__main__':
    main()