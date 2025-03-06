def dobro(n):
    return n*2
def triplo(n):
    return n*3
def mult10(n):
    return n*10

print("Quantos Numeros?\n")
tamanho = int(input())

numeros = []

for i in range(tamanho):
    print("Digite um numero:")
    num = int(input())
    numeros.append(num)

print("\nVocê quer Dobrar,Triplicar ou multiplicar por 10? (2,3,10)\n")
escolha = int(input())
print("\n")

resultado = None


match escolha:
    case 2:
        resultado = map(dobro,numeros)
        print(f"Lista Normal:{numeros}")
        print(f"Lista Modificada:{list(resultado)}")
    case 3:
        resultado = map(triplo,numeros)
        print(f"Lista Normal:{numeros}")
        print(f"Lista Modificada:{list(resultado)}")
    case 10:
        resultado = map(mult10,numeros)
        print(f"Lista Normal:{numeros}")
        print(f"Lista Modificada:{list(resultado)}")