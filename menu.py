import sqlite3
from tkinter import *

#configuracion de la root
root = Tk()
root.title("Lunch bar - Menú")
root.resizable(0,0)
root.config(bd=25,relief="sunken")

Label(root, text="   Lunch bar   ", fg = "darkgreen",font=("Times New Roman",28,"bold italic")).pack()
Label(root, text="Menú del día", fg = "green",font=("Times New Roman",24,"bold italic")).pack()

#separacion de titulos y categorias
Label(root,text="").pack() #espacio

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

#buscar categorias y datos de la bd

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    
for categoria in categorias:
        print(categoria[1])
        Label(root,text=categoria[1],fg = "black",font=("Times New Roman",20,"bold italic")).pack()
        
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0]))
        for plato in platos:
            Label(root,text=plato[1],fg = "gray",font=("Verdana",15,"italic")).pack()
        Label(root,text="").pack()


conexion.close()

#price
Label(root,text="15 soles",fg = "darkgreen",font=("Verdana",20,"bold italic")).pack(side=RIGHT)


#bucle principal
root.mainloop()