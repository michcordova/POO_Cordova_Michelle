import mysql.connector

connection = {
    "host": 'localhost',
    "user": 'root',
    "password": '',
    "database": 'control1',
}

try:
    connection = mysql.connector.connect(**connection)
    print("Conexión exitosa")
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
    exit()

cursor = connection.cursor()

#SELECT
cursor.execute("SELECT * FROM alumnos")
alumnos = cursor.fetchall()
print("Datos de la tabla 'alumnos':")
for alumno in alumnos:
    print(alumno)

#INSERT
alumno_nuevo = ("MichMich", 19, "Su casa", 1)
cursor.execute("INSERT INTO alumnos (nombre, edad, direccion, id_maestro) VALUES (%s, %s, %s, %s)", alumno_nuevo)
connection.commit()
print("\nNuevo alumno insertado")

#UPDATE
cursor.execute("UPDATE alumnos SET edad = 20 WHERE nombre = 'MichMich'")
connection.commit()
print("\nEdad actualizada")

#DELETE
cursor.execute("DELETE FROM alumnos WHERE nombre = 'MichMich'")
connection.commit()
print("\nAlumno eliminado")



cursor.close()
connection.close()
