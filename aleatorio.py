#-*- coding: utf-8 -*-
#Meu Décimo sétimo Programa
#Trabalhando com  modularização
import random

def geraListaInteiro(tam):
    lista = []
    for i in range(tam):
        lista.append(random.randint(0, tam))
    return lista
    
