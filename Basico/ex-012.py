#Contagem de palavra

x = str(input("Escreva algo: "))

y = x.split()

count = 0

for i in y:
    print(f"{i}")
    
print(f"Numero de palavras: {len(y)}")

