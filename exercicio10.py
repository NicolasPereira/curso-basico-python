#-*- coding: utf-8 -*-
'''
Escreva um programa que leia um arquivo multi-fasta e armazene em um dicionário:
cabeçalho da sequência como a chave e a sequência como valor.
'''

arquivo = open("Arquive.fasta")
linhas = arquivo.readlines()
multifasta = {}
for linha in linhas:

    if linha[0] == ">":
        seqAtual = linha[1:].strip()
        multifasta[seqAtual] = ""
    else:
        multifasta[seqAtual] = multifasta[seqAtual]+linha.strip()

print (multifasta)
