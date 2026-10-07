# Sistema básico de gestión de inventario
# Proyecto realizado para demostrar el uso de Git

inventario = []


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(producto)

    print("Producto agregado correctamente.")


def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n--- INVENTARIO ---")

    for producto in inventario:
        print(
            f"Producto: {producto['nombre']} | "
            f"Cantidad: {producto['cantidad']} | "
            f"Precio: ${producto['precio']}"
        )

def buscar_producto():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")

    encontrado = False

    for producto in inventario:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print("\nProducto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: ${producto['precio']}")
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


def menu():
    while True:
        print("\n===== GESTOR DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


menu()