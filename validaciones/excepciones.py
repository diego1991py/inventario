"Modulo para manejo de excepciones"

class VerificarDatos(Exception):
    pass

def verificar_mayores(id, precio, cantidad): #Verificación de valores negativos o iguales a Cero
    if not id > 0 or not precio > 0  or not cantidad >= 0:
        raise VerificarDatos("Los datos tiene que ser mayor que Cero")
