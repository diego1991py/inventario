"Clase Producto"

"""Atributos:
        id (int) : autoincremento
        nombre (str) : unico
        precio (float) : mayor que cero
        cantidad (int) : mayor o igual que cero"""

"""Métodos:
        __str__ : convertir a str
        to_dict : convertir a diccionario para enviar a csv"""


class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.precio} - {self.cantidad}"
    
    def to_dict(self):
        return{
            "id " : self.id,
            "nombre" : self.nombre,
            "precio" : self.precio,
            "cantidad" : self.cantidad
        }