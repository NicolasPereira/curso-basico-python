#-*- coding: utf-8 -*-
'''
Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
'''

num1 = float(input("Digite o primeiro numero: "))
operador = input("Digite o operador: ")
num2 = float(input("Digite o segundo numero: "))

#Verifica operadores
if operador == "+":
    resultado = num1 + num2
    print(resultado)
elif operador == "-":
    resultado = num1 - num2
    print(resultado)
elif operador == "/":
    resultado = num1 / num2
    print(resultado)
elif operador == "*":
    resultado = num1 * num2
    print(resultado)
elif operador == "**":
    resultado = num1 ** num2
    print(resultado)
elif operador == "%":
    resultado = num1 % num2
    print(resultado)
else:
    print("Operador não valido")
