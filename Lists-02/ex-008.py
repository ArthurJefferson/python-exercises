import time

x = str(input("Digite algo:"))

print("Vou manipular seu texto\n")

time.sleep(1)

print(f"Seu texto normal: {x}\n")
print(f"Seu texto em maiúsculo: {x.upper()}\n")
print(f"Seu texto em minúsculo: {x.lower()}\n")
print(f"Seu texto em título: {x.title()}\n")
print(f"Seu texto em capitalize: {x.capitalize()}\n")
print(f"Seu texto em swapcase: {x.swapcase()}\n")
print(f"Seu texto com split: {x.replace("Oi")}\n")
