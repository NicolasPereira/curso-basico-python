#-*- coding: utf-8 -*-
#Meu Décimo Programa
#Trabalhando com Strings

a = "Nicolas"
b = "Rocha"

concatenar = a +" "+ b + "\n"

tamanho = len(concatenar)

print ("Nome Completo: " +concatenar)
print ("Total de Caracteres do Nome é : %d"%(tamanho))
'''
    Ao utilizar nomeVariavel[posicao], você seleciona qual a
    letra que gostaria de pegar naquele index. Lembrando
    que o index inicial é 0.
'''
print("Letra inicial do Nome: " +a[0])
print("Letra inicial do Sobrenome: " +b[0])
print("4 Primeiras letras do Nome: "+a[0:4])
print("----Funções----")

#Função que deixa tudo minisculo
print("Lower: " +concatenar.lower())

#Função que deixa tudo maisculo
print("Upper: " +concatenar.upper())

#Remove espaço inicio e fim e caractere especial
print("Strip: " +concatenar.strip())

print()
print("-----------------------------")
print()

'''
A função split cria uma lista com a string conforme parametro
neste caso o parametro foi o espaço
'''
minhaString = "O rato roeu a roupa do rei de roma"
minhaLista = minhaString.split(" ")
print(minhaLista)

'''
A funcao find  busca dentro da string, essa função retorna o indice da posição
da string procurada
'''

busca = minhaString.find("roupa")

print("A palavra procurada está no index: %d" %(busca))

'''
A funcao replace substitui uma parte da string por outro texto desejado
'''

stringReplace = minhaString.replace("do rei","da rainha")
print(stringReplace)
