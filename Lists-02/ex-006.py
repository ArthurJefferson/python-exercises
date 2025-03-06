numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def minus(n):
    return n - 11

def mais(n):
    return n + 10
adc = map(mais, numeros)
menos = map(minus, numeros)
print(list(numeros))
print(list(adc))
print(list(menos))