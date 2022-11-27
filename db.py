import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="SharkD",
    passwd="password",
    database="prueba"
)

cursor = midb.cursor()

cursor.execute("SELECT * FROM Usuario")

#resultado = cursor.fetchall()
resultado = cursor.fetchone()

print(resultado)