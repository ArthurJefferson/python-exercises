#LISTA ORDENADA E MUTAVEL, PERMITE DUPLICAÇÕES
lista = ["Carro", 2, True, 2.6, 'G']
print(lista)
print(type(list))
for lista in lista:
    print(lista)
print("-"*40)

#TUPLA É IMUTAVEL E ORDENADA, PERMITE DUPLICAÇÕES
tupla = ("Carro", 5, 2.7, True, 'Q')
print(tupla)
print(type(tupla))
for tupla in tupla:
    print(tupla)
print("-"*30)

#DICIONARIO É ORDENADO E MUTAVEL, NÃO PERMITE DUPLICAÇÕES
dicionario = {"Nome": "João", "Idade": 15, "Altura" : 1.70}
print(dicionario)
print(type(dicionario))
for dicionario in dicionario:
    print(dicionario)
print("-"*30)

#SÃO COLEÇÕES INORDENADAS E INDEXADAS, NENHUM MEMBRO DUPLICADO
conjunto = {"Carro", 2, 2.6}
print(conjunto)
print(type(conjunto))
for conjunto in conjunto:
    print(conjunto)
