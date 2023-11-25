def fibonacci(numero):
    if numero == 0 or numero == 1:
        return 1
    return fibonacci(numero-1) + fibonacci(numero-2)
print(fibonacci(4))