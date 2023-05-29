import sqlite3


# clase principal de manejar la informacion de las credenciales de la base de datos Credenciales.db

class Credenciales:

    def __init__(self) -> None:

        conexion = sqlite3.connect("Credenciales.db")
        cursor = conexion.cursor()
        cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"')
        self.tablas = [name[0] for name in cursor.fetchall()]
        conexion.close()

    def crear(self, filetabla):

        conexion = sqlite3.connect("Credenciales.db")
        cursor = conexion.cursor()
        cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"')
        self.tablas = [name[0] for name in cursor.fetchall()]
        find = filetabla not in self.tablas

        if find and not (filetabla.isspace()) and len(filetabla) > 0:
            cursor.execute(f"CREATE TABLE '{filetabla}'"
                           "(ID INTEGER, TITULO VARCHAR(100), 'CORREO_O_NUMERO' VARCHAR(100), PASSWORD VARCHAR(20))"
                           )
            self.tablas.append(filetabla)
        conexion.commit()
        conexion.close()

        return find

    def write(self, filetabla, lista):

        conexion = sqlite3.connect("Credenciales.db")
        cursor = conexion.cursor()

        cursor.executemany(
            f"INSERT INTO {filetabla!r} VALUES(?, ?, ?, ?) ", [tuple(lista)])

        conexion.commit()
        conexion.close()

    def read(self, ejecutar=None):

        conexion = sqlite3.connect("Credenciales.db")
        cursor = conexion.cursor()

        cursor.execute(ejecutar)
        contenido = cursor.fetchall()

        conexion.commit()
        conexion.close()
        return contenido

    def ultimo_id(self, nameTabla):

        conexion = sqlite3.connect("Credenciales.db")
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT ID FROM {nameTabla!r} WHERE ID=(SELECT MAX(ID) FROM {nameTabla!r})")
        idmax = cursor.fetchone()
        conexion.close()
        print(idmax)
        return 1 if idmax is None else idmax[0] + 1

    def update(self, ejecutar, lista):

        conexion = sqlite3.connect("Credenciales.db")
        cursor = conexion.cursor()

        cursor.execute(ejecutar, lista)

        conexion.commit()
        conexion.close()

    def delete(self, ids, nameTabla):

        conexion = sqlite3.connect("Credenciales.db")
        cursor = conexion.cursor()

        for id in ids:
            cursor.execute(f"DELETE FROM {nameTabla!r} WHERE ID='{id}'")

        conexion.commit()
        conexion.close()

    def deleteTabla(self, nameTabla):

        conexion = sqlite3.connect("Credenciales.db")
        cursor = conexion.cursor()
        cursor.execute(f'DROP TABLE IF EXISTS {nameTabla!r}')
        conexion.commit()
        conexion.close()
