#-*- coding: utf-8 -*-
'''
Faça um programa que diga se um usuário é maior ou menor de idade.
Se for maior que 18, imprima "maior de idade".
Se for menor que 18, imprima "menor de idade".
Verifique se a idade é um numero inteiro positivo
'''
idade = int(input("Digite sua idade: "))

# Verifique se usuario eh maior de idade ou menor de idade
if idade >= 18:
    print("maior de idade")
elif idade > 0 and idade < 18:
    print("menor de idade")
else:
    print("Idade invalida")
