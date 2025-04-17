"Clase Producto"

"""Atributos:
        self.lista_producto (array) : vacio para agregar los productos nuevos"""

"""Métodos:
        cargar_productos : Carga los productos existentes en el csv
        agregar_producto : Agrega los productos nuevos a la lista vacia, para ser cargados al csv
        guardar_productos : Envía los productos al CSV
        ver_productos :  Carga la lista de productos desde el csv, mostrandolos visualmete
        """

from producto import Producto
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
            
        
    def nuevo_producto(self, producto): #Agrega el producto a la lista
        self.lista.append(producto)
        return self.lista
                
    
    def guardar_productos(self): #Guarda la lista en csv
        with open(ruta_archivo, "w", encoding="utf-8", newline="") as archivo:
            campos = ["id","nombre","precio","cantidad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for linea in self.lista:
                escritor.writerow(linea)

    def ver_productos(self): #Imprime los productos cargados en la lista
            for linea in self.lista:
                for clave, valor in linea.items():
                    print(f"{clave} : {linea[clave]}")
            
                
        

nuevo_pro = Producto(1,"CPU",500000, 10)
nuevo_pro_dos = Producto(2,"Teclado",25000, 5)
convertir = nuevo_pro.to_dict()
convertir_dos = nuevo_pro_dos.to_dict()

mi_inve = Inventario()

mi_inve.nuevo_producto(convertir)

mi_inve.guardar_productos()

mi_inve.nuevo_producto(convertir_dos)
mi_inve.guardar_productos()

mi_inve.ver_productos()


