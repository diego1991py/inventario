"Clase Producto"

"""Atributos:
        self.lista_producto (array) : vacio para agregar los productos nuevos"""

"""Métodos:
        cargar_productos : Carga los productos existentes en el csv
        agregar_producto : Agrega los productos nuevos a la lista vacia, para ser cargados al csv
        guardar_productos : Envía los productos al CSV
        ver_productos :  Carga la lista de productos desde el csv, mostrandolos visualmete
        """

import os
import csv
from producto import Producto

ruta_script = os.path.dirname(__file__)
ruta_archivo = os.path.join(ruta_script, "..\\data", "archivo.csv") 
os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

class Inventario:
    def __init__(self):
        self.lista_producto = []

    def cargar_productos(self):
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                reader = csv.DictReader(archivo)
                for fila in reader:
                    producto = Producto(
                            id=fila["id"],
                            nombre=fila["nombre"],
                            precio=float(fila["precio"]),
                            cantidad=int(fila["cantidad"])
                        )
                    self.lista_producto.append(producto)

    def agregar_producto(self, producto):
        ids_existentes = [p.id for p in self.lista_producto]
        if producto.id not in ids_existentes:
            self.lista_producto.append(producto)
            return True
        return False

        
    def guardar_productos(self):
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            campos = ["id", "nombre", "precio", "cantidad"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows([p.to_dict() for p in self.lista_producto])

        
    def ver_productos(self):
        for producto in self.lista_producto:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")


