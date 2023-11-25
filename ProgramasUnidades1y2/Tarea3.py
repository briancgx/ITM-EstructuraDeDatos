def polinomio(number):
    x=0
    for i in range(1, number):
        for j in range(1,number):
            x += i+j
    for i in range(1, number):
        for j in range(1,number):
            for k in range(1,number):
                x += i*j*k
    return x

def constanste():
    x = 50
    x += x
    return x

