num = [1,2,3,4,5,6,7,8,9,10]

def plus(x):
    return x + x

resultado = map(plus, num)

print(list(resultado))