#-*- coding: utf-8 -*-
#Meu Vigésimo terceiro Programa
#Trabalhando com  Graficos e Visualização de Dados
#importando a biblioteca
import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,2]


titulo="Gráfico de Barras - Compare"
eixox= "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Setar dados no graficos
plt.plot(x,y,color="k", linestyle="-")
plt.scatter(x,y, label = "Meus pontos", color="r", marker=".", s=100)
#mostrar legenda
plt.legend()
#mostrar grafico
plt.show()
plt.savefig("figura1.png",dpi=300)
