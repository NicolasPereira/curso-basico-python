#-*- coding: utf-8 -*-
#Meu Décimo sétimo Programa
#Trabalhando com modularização

#calcular media, mediana, moda
'''
from statistics import *
jeito facil
mean(lista)
median(lista)
mode(lista)
'''

def media(lista):
    #media = mean(lista)
    media = sum(lista)/float(len(lista))
    return media

def mediana(lista):
    #mediana = median(lista)
    listaOrdenada = sorted(lista)
    tam = len(listaOrdenada)

    if tam % 2 == 0:
        mediana = (listaOrdenada[int(tam/2)] + listaOrdenada[int((tam/2)-1)])/2
    elif tam % 2 ==1:
        mediana = listaOrdenada[int((tam/2))]
    return mediana

def moda(lista):
    #moda = mode(lista)
    lista_dic = {}
    for l in lista:
            if l not in lista_dic:
                lista_dic[l] = 1
            else:
                lista_dic[l] += 1

    maior_repeticao = max(lista_dic.values())

    for i in lista_dic:
            if lista_dic[i] == maior_repeticao:
                moda = i
                return moda
