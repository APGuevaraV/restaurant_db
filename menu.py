import sqlite3
from tkinter import *

#configuracion de la root
root = Tk()
root.title("Lunch bar - Menú")
root.resizable(0,0)
root.config(bd=10,relief="sunken",bg="#fb05a9")

frame = Frame(root,bd=10,background="#f9f3a9")
frame.pack(fill=BOTH,side="top")

Label(frame, text="   Lunch bar   ",bg="#f9f3a9", fg = "darkgreen",font=("Brusher",28,"bold italic")).pack()
Label(frame, text="Menú del día",bg="#f9f3a9", fg = "green",font=("Brusher",24,"bold italic")).pack()

#separacion de titulos y categorias
Label(frame,bg="#f9f3a9",text="").pack() #espacio

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

#buscar categorias y datos de la bd

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    
for categoria in categorias:
        
        Label(frame,text=categoria[1],bg="#f9f3a9" ,fg = "black",font=("A little Sunshine",20,"bold italic")).pack()
        
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0]))
        for plato in platos:
            Label(frame,text=plato[1],bg="#f9f3a9" ,fg = "gray",font=("A little Sunshine",15,"italic")).pack()
        Label(frame,bg="#f9f3a9", text="").pack()


conexion.close()

#price
Label(frame,text="15 soles",bg="#f9f3a9",fg = "darkgreen",font=("A little Sunshine",20,"bold italic")).pack(side=RIGHT)


#bucle principal
root.mainloop()