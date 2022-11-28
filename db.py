import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="SharkD",
    passwd="250893",
    database="prueba"
)

cursor = midb.cursor()

#cursor.execute("SELECT * FROM Usuario")

#resultado = cursor.fetchall()
#resultado = cursor.fetchone()

#consultar como esta la tabla
#cursor.execute("show create table Usuario")

#insertar datos
# sql = "INSERT INTO Usuario (id, email, username, edad) VALUES (%s,%s, %s, %s)"
# values = (2,"liloliol@hotmail.com","SharkD", 28)
# cursor.execute(sql, values)

#actualizar datos
# sql = "UPDATE Usuario set email = %s where id = %s"
# values = ("pepe@ppe.com",1)
# cursor.execute(sql, values)

#eliminar datos
sql = "DELETE FROM Usuario where id = %s"
values = (1,)
cursor.execute(sql, values)

midb.commit()
print(cursor.rowcount, "registros eliminados")