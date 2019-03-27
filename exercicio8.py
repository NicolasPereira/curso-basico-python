#-*- coding: utf-8 -*-
'''
Escreva um programa que receba uma sequência digitada pelo usuário e a salve num arquivo no formato fasta.
'''

seq = input("Digite uma sequencia: ")

arquivo = open("Arquive.fasta","w")

arquivo.write(">seq\n")
arquivo.write(seq)

arquivo.close()

print("success")
