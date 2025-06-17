import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute('''
                CREATE TABLE categoria(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL)   
                   ''')
    except sqlite3.OperationalError: 
        print('La tabla de categoría ya existe')
    else:
        print('La tabla categoría se creó correctamente')
    
    try :
        cursor.execute('''
                   CREATE TABLE plato(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL, 
				categoria_id INTEGER NOT NULL,
				FOREIGN KEY(categoria_id) REFERENCES categoria(id))
                   ''')
    except sqlite3.OperationalError:
        print('La tabla plato ya existe')
    else:
        print('Tabla plato se creaó correctamente')
    
    conexion.close()
    

def agregar_categoria():
    categoria = input("Nombre de la nueva categoria? \n > ")
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO categoria VALUES (null,'{}')".format(categoria))
        
    except:
      print(f"La categoría {categoria} ya existe") 
    else:
        print (f"La categoría {categoria} creada correctamente") 
    
    conexion.commit()
    conexion.close()
    
def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria para añadir el plato:\n")
    for categoria in categorias:
        print("[{} {}]".format(categoria[0], categoria[1]))
    categoria_usuario = int(input("> "))
    nombre_plato = input(">Nombre plato :")
    try:
        cursor.execute("INSERT INTO plato VALUES (null,'{}',{})".format(nombre_plato,categoria_usuario))
        
    except:
      print(f"El plato {nombre_plato} ya existe") 
    else:
        print (f"El plato {nombre_plato} fue creada correctamente") 
    
    
    conexion.commit()
    conexion.close()
        
def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0]))
        for plato in platos:
            print("\t{}".format(plato[1]))


crear_bd()

#Menú

while True:
    print("\n Bienvenido al gestor del restaurante")
    opcion = input("Introduce una opcion :\n [1] Agregar una categoria \n [2] Agregar un plato \n [3] Mostrar Menú \n [4] Salir del programa\n >")
    
    if opcion == "1":
        agregar_categoria()
        
    elif opcion == "2":
        agregar_plato()
        
    elif opcion == "3":
        mostrar_menu()
        
    elif opcion == "4":
        print("\n Hasta luego!")
        break;
    
    else:
        print("Opción incorrecta")