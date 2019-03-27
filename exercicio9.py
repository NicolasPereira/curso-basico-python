#-*- coding: utf-8 -*-
'''
Escreva um programa que exiba um menu e pergunte o que o usuário deseja fazer.
Se o usuário digitar 1, o programa deve chamar uma função que abre um arquivo de texto.
Se o usuário apertar 2, o programa deve imprimir o conteúdo do arquivo lido anteriormente.
Se o usuário apertar 3, o programa deve ser fechado.
'''
menu = 0
def abrirArquivo():
    nome = input("Digite o nome do Arquivo que deseja abrir: ")
    arquivo = open(nome)
    return arquivo

def lerArquivo(arquivo):
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())

while menu != 3:
    print()
    print("------------------------------------------")
    print("|Digite 1 para abrir um arquivo de texto |")
    print("|Digite 2 para ler o arquivo aberto      |")
    print("|Digite 3 para sair do programa          |")
    print("------------------------------------------")
    print()
    menu = int(input("Digite uma das opções: "))

    if menu == 1:
        arquivo = abrirArquivo()
    elif menu == 2:
        lerArquivo(arquivo)
