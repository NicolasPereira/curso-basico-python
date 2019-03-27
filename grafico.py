#-*- coding: utf-8 -*-
#Meu Décimo nono Programa
#Trabalhando com  Graficos e Visualização de Dados
#importando a biblioteca
import matplotlib.pyplot as plt

x = [1,2,5]
y = [2,3,7]


#Titulo
plt.title("Meu Primeiro Grafico")
#Eixo
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

#Setar dados no graficos
plt.plot(x,y)

#mostrar grafico
plt.show()
