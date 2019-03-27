#-*- coding: utf-8 -*-
#Meu Vigésimo quarto Programa
#Trabalhando com  boxplot
#importando a biblioteca
import matplotlib.pyplot as plt
import random
vetor = []
for i in range(10):
    numeroAleatorio = random.randint(0,50)
    vetor.append(numeroAleatorio)
    print(vetor)
plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
