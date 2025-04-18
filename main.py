from models.producto import Producto
from models.inventario import Inventario


inventarios = Inventario()

while True:
    print("\n--Bienvenido--")
    print("Por favor elegir una opción")
    print("1 - Agregar producto\n2 - Para guardar productos\n3 - Para ver lista de productos\n0 para salir")
    opcion = input("\nPor favor selecciones una opción: ").strip()

    if not opcion in ["0","1","2","3"]:
        print(f"{opcion} no es la opción correcta")

    elif opcion == "1":
            id = int(input("Agregar ID: ").strip())
            nombre = input("Agregar nombre: ").strip()
            precio = float(input("Agregar precio: ").strip())
            cantidad = int(input("Agregar cantidad: ").strip())

            productos = Producto(id, nombre, precio, cantidad)
            convertir = productos.to_dict()
            inventarios.nuevo_producto(convertir)
         
    elif opcion == "2":
        inventarios.guardar_productos()
        print(f"Se agrego el producto {productos.__str__()}")

    elif opcion == "3":
         inventarios.ver_productos()
        