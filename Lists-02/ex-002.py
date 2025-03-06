def dobro(n):
    return n*10

num = [1,2,3,4,5,6,7,8,9]

resultado = map(dobro,num)

print(list(resultado))