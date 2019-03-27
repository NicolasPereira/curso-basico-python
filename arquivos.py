#-*- coding: utf-8 -*-
#Meu Décimo terceiro Programa
#Trabalhando com arquivos

arquivo = open("arquivo.txt")
#Lê todas as linhas do arquivos e coloca em uma lista
linhas = arquivo.readlines()
print(linhas)
print("---------------------------")
#Imprime linha por linha
print("Mostrando Linha por Linha")
print()
for linha in linhas:
    print(linha)
print("---------------------------")
#Fechar o arquivo
arquivo.close()

#Criar um arquivo
w = open("arquivo2.txt","a")

w.write("Eu escrevi no python\n")
#Fechar o Arquivo
w.close()
