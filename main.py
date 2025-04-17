from models.producto import Producto
from models.inventario import Inventario

inven = Inventario()

while True:
    while True:
        print("\n--Bienvenido--")
        print("Por favor elegir una opción")
        print("1 - Agregar tarea\n2 - Para guardar la tarea\n0 - Para salir")
        opcion = input("\nPor favor selecciones una opción: ").strip()