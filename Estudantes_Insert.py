import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="12345",
  database="saladeaula"
)

mycursor = mydb.cursor()

valores = [1, 2, 3, 4, 12, 13, 14, 15, 17, 18, 20, 21, 22, 23, 24, 25, 28, 29]
print(len(valores))
lista = []

with open('student-mat.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if len(row[0]) < 3:  # Ignora nome das colunas
            lista.clear()
            for col, val in enumerate(valores):
                lista.append(row[val])
            sql = 'INSERT INTO estudante(sexo, idade, endereco, tamfamilia, tempoviagem, tempoestudo, materiasperdidas, reforco, pagar, extracurriculares, superior, internet, namoro, relfamilia, tempolivre, vidasocial, saude, faltas)   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            val = (lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10], lista[11], lista[12], lista[13], lista[14], lista[15], lista[16], lista[17], )
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")

