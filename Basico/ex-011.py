#FATORIAL

x = int(input("Escreva um número:"))
soma = 1
for i in range(1, x + 1):
    soma = soma * i 
    
print(f"{x}! = {soma}")    