from models.producto import Producto
from models.inventario import Inventario


inventarios = Inventario()

while True:
    print("\n--Bienvenido--")
    print("Por favor elegir una opción")
    print("1 - Agregar producto\n2 - Para ver lista productos\n3 - Para ver un producto por ID\n0 para salir")
    opcion = input("\nPor favor selecciones una opción: ").strip()

    if not opcion in ["0","1","2","3"]:
        print(f"{opcion} no es la opción correcta")

    elif opcion == "1":
            
            id = inventarios.ver_id()
            nombre = input("Agregar nombre: ").strip()
            precio = float(input("Agregar precio: ").strip())
            cantidad = int(input("Agregar cantidad: ").strip())

            productos = Producto(id, nombre, precio, cantidad)
            convertir = productos.to_dict()
            inventarios.nuevo_producto(convertir)
            print(f"Se agrego el producto {productos.__str__()}")
         
    elif opcion == "2":
         inventarios.ver_productos()

    elif opcion == "3":
         ver_id = input("Ingresar ID para ver producto: ").strip()
         resultado = inventarios.ver_producto_id(ver_id)
         if resultado:
            print(f"id= {resultado["id"]}\nnombre= {resultado["nombre"]}\nprecio= ${resultado["precio"]}\ncantidad= {resultado["cantidad"]} unidades")
         else:
            print(f"el producto con id {ver_id} no existe")
    elif opcion == "0":
         print("Gracias por visitarnos")
         break
        