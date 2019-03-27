#-*- coding: utf-8 -*-
#Meu Décimo segundo Programa
#Trabalhando com dicionarios

meuDicionario = {"A":"ANA LUIZA","B":"BRUNO","C":"CAROL"}
print("Todo dicionario:")
print(meuDicionario)
print()
print("Somente letra A")
print(meuDicionario["A"])
print()
print("Somente letra B")
print(meuDicionario["B"])
print()
print("Somente letra C")
print(meuDicionario["C"])
print()
print("Percorrendo o Dicionario")

#Percorrer os itens do dicionario - TUPLA
for i in meuDicionario.items():
    print (i)

print()
print("Percorrendo as chaves")
for k in meuDicionario.keys():
    print(k)

print()
print("Percorrendo os valores")
for v in meuDicionario.values():
    print(v)
