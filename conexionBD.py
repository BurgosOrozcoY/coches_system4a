import mysql.connector
from tkinter import *
from tkinter import messagebox

try:
    conexion = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "",
        database = "bd_coches"     
    )
    cursor = conexion.cursor(buffered = True)

except:
    messagebox.showerror("Error de conexión", "No se pudo conectar a la base de datos. Por favor, inténtelo más tarde.")