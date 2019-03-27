#-*- coding: utf-8 -*-
#Meu Vigésimo primeiro Programa
#Trabalhando com  Graficos e Visualização de Dados
#importando a biblioteca
import matplotlib.pyplot as plt

x1 = [1,3,5,7,9] #qnt de barras
y1 = [2,3,7,1,0] #tamanho das barras


x2 = [2,4,6,8,10] #qnt de barras
y2 = [5,1,3,7,4] #tamanho das barras

titulo="Gráfico de Barras - Compare"
eixox= "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Setar dados no graficos
plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")

#mostrar legenda
plt.legend()
#mostrar grafico
plt.show()
