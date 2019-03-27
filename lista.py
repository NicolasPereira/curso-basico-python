#-*- coding: utf-8 -*-
#Meu Décimo Primeiro Programa
#Trabalhando com Listas

minhaLista = ["abacaxi","melancia","morango"]
minhaLista2 = [1,2,3,4,5]
minhaLista3 = ["abacaxi","melancia",1,9.29,True]

print("Lista:")
#Percorrendo a Lista
for item in minhaLista:
    print(item)
#Verificar tamanho da lista
print("Tamanho da lista: %d" %(len(minhaLista)))
print()

#Adicionando itens a Lista -> Append
print("-----Adicionando item da lista------")
minhaLista.append("limão")
print()
print("Nova Lista:")
for item in minhaLista:
    print(item)
print("Tamanho da lista: %d" %(len(minhaLista)))

print()
print("----Removendo Item da Lista----")
print("Lista:")
print(minhaLista3)

#Remover um item da lista
del minhaLista3[0]
print("Lista pós exclusão:")
print(minhaLista3)
print()

print("---Verificaindo se existe o item---")
#Verificar se existe um termo/valor na lista
if 3 in minhaLista2:
    print("3 está na lista")
else:
    print("Não está na lista")

print()

print("--- Ordenando Listas ---")

#Método Sort
print("Método sort:")
minhaLista2.sort()
print(minhaLista2)
print("Método sort decrescente:")
minhaLista2.sort(reverse = True)
print (minhaLista2)
print("Método reverse:")
minhaLista3.reverse()
print(minhaLista3)
