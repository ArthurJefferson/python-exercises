enemy = ["Skeleton", "Zombie", "Pigman", "Enderman"]
blocks = ["Bloco de Diamante","Bloco de Grama", "Obisidian"]

print("Qual lista você quer acessar? (enemy ou blocks)\n")

# Função de print
def Slist(lst):
    cont = 0
    for n  in enumerate(lst):
            print(f"{cont} - {lst[cont]}")
            cont = cont + 1

escolha = input()
try:
    if escolha == "blocks":
        print("-"*40)
        Slist(blocks)
    elif escolha == "enemy":
        print("-"*40)
        Slist(enemy)
    else:
        print("Error")
        raise ValueError
            
except ValueError:
    print("-"*40)
    print("Escolha Inválida")
print("-"*40)

#Troca de Index
x = input("Quer trocar alguma lista (s/n)?:").lower()
if x == "s":
    x = input("Qual lista?")
    if x == "enemy":
        Slist(enemy)
        x = int(input("Qual você quer?:"))
        print(f"\nVocê quer trocar o {enemy[x]} por?:")
        y = str(input())
        enemy[x] = y
        print("-"*30)
        Slist(enemy)
    
    if x == "blocks":
        Slist(blocks)
        x = int(input("Qual você quer?:"))
        print(f"\nVocê quer trocar o {blocks[x]} por?:")
        y = str(input())
        blocks[x] = y
        print("-"*30)
        Slist(blocks)
else:
    print("Inválido")
