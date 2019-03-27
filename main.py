#-*- coding: utf-8 -*-
#Meu Décimo sétimo Programa
#Trabalhando com  modularização
import media as m
import aleatorio as a

lista = a.geraListaInteiro(10)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print("Minha Lista:\n")
print (lista)
print()
print ("A média da minha lista é: " + str(media))
print()
print ("A mediana da minha lista é: " + str(mediana))
print()
print ("A moda da minha lista é: " + str(moda))
