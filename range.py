#-*- coding: utf-8 -*-
#Meu Oitavo Programa
#Trabalhando com RANGE

'''
Imprime no console os valores de 10 digitos sequenciais
No caso abaixo seria do valor 0 até 9
'''
print("Range de 10 digitos")
for i in range(10):
    print (i)
print("-------------------")

#Imprime no console os valores do intervalo do numero 10 até numero 19
print("Range de intevalo do numero 10 ao 19")
for x in range(10,20):
    print (x)

print("-------------------")
'''
O terceiro parametro é a forma que ira percorrer o range, mostrando no
intervalo de 2 em 2 numeros
'''
print("Range de intevalo do numero 10 ao 19 com intervalo de 3 numeros")
for x in range(10,20,3):
    print (x)
print("-------------------")
