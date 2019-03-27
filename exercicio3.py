#-*- coding: utf-8 -*-
'''
Faça um programa que resolva uma equação de segundo grau
'''
from math import sqrt

a = float(input("Digite o valor A"))
b = float(input("Digite o valor de B"))
c = float(input("Digite o valor de C"))

delta = b**2 - 4*a*c
raizDelta = sqrt(delta)

x1 = (-b + raizDelta)/(2*a)
x2 = (-b - raizDelta)/(2*a)

print("x1 = %.2f" %(x1))
print("x2 = %.2f" %(x2))
