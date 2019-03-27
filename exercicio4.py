#-*- coding: utf-8 -*-
'''
Escreva um programa que ordene uma lsita numérica com três elementos.
'''
lista = [500,1920,1,22,13,928]
#Com a função sorted
fSorted = sorted(lista)

#selection sort
print(fSorted)
for i in range(len(lista)):
    menor = i

    for j in range(i+1,len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

print (lista)
