"Clase Producto"

"""Atributos:
        self.lista_producto (array) : vacio para agregar los productos nuevos"""

"""Métodos:
        cargar_productos : Carga los productos existentes en el csv
        agregar_producto : Agrega los productos nuevos a la lista vacia, para ser cargados al csv
        guardar_productos : Envía los productos al CSV
        ver_productos :  Carga la lista de productos desde el csv, mostrandolos visualmete
        """
import os, csv

ruta_archivo = os.path.join(os.path.dirname(__file__), "..\\data", "archivo.csv")

class Inventario:
    def __init__(self):
        self.lista = []

    def cargar_productos(self): #Carga productos desde el archivo
        self.lista = []
        with open(ruta_archivo, "r", encoding= "utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for linea in lector:
                self.lista.append(linea)
        return self.lista
    
    def ver_id(self): #Lee la longitud de la lista y suma 1 para el ID, evita duplicados
         self.cargar_productos()
         nuevo_id = len(self.lista)+1
         return nuevo_id              
                         
            
        
    def nuevo_producto(self, producto): #Agrega el producto a la lista
                if producto["id"] in self.lista:
                     return "ID ya existe"
                else:
                   self.lista.append(producto)
                   self.guardar_productos()
                return self.lista
                
    
    def guardar_productos(self): #Guarda la lista en csv
        with open(ruta_archivo, "w", encoding="utf-8", newline="") as archivo:
            campos = ["id","nombre","precio","cantidad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for linea in self.lista:
                    escritor.writerow(linea)

    def ver_productos(self): #Imprime los productos cargados en la lista
            self.cargar_productos()
            for linea in self.lista:
                print(f"ID= {linea["id"]}\nnombre= {linea["nombre"]}\nprecio= ${linea["precio"]}\ncantidad= {linea["cantidad"]} unidades\n------")
            
                
