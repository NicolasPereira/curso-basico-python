#-*- coding: utf-8 -*-
#Meu Décimo oitavo Programa
#Trabalhando com  MySQL and Python

import MySQLdb

host = "localhost"
user = "root"
password = "root"
db = "meubanco"
port = 3306

con = MySQLdb.connect(host,user,password,db,port)


mycursor = con.cursor()

mycursor.execute("select nome_alunos from alunos")

myresult = mycursor.fetchall()

for x in myresult:
    print("Nome do aluno: "+ str(x))
