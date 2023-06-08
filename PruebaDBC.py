import dbconexion as db

conexion = db.con.cursor()
conexion.execute("Select * from cliente")
result = conexion.fetchall()

objeto = []
nombresColumnas = [column[0] for column in conexion.description]
for record in result:
    objeto.append(dict(zip(nombresColumnas,record)))
conexion.close
print(objeto)
