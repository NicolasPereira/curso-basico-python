#-*- coding: utf-8 -*-
#Meu Vigésimo Programa
#Trabalhando com  Graficos e Visualização de Dados
#importando a biblioteca
import matplotlib.pyplot as plt

x = [1,2,3,4,5] #qnt de barras
y = [2,3,7,1,10] #tamanho das barras

titulo="Gráfico de Barras"
eixox= "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Setar dados no graficos
plt.bar(x,y)

#mostrar grafico
plt.show()
