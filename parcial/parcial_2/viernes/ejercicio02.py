""" #EJERCICIO 2 Debes desarrollar una aplicación para administrar el inventario de una cadena de tiendas de electrónica. Cada local tiene su
propio inventario de productos, identificados por un código único. Cuando un cliente solicita un producto, se debe buscar su código en el
inventario de la tienda correspondiente para verificar si está disponible. Hay que implementar un algoritmo de búsqueda lineal para encontrar
un código de producto específico en el inventario de cada tienda. El programa debe: Permitir al usuario ingresar el código del producto que
está buscando. Permitir al usuario seleccionar la tienda en la que desea buscar el producto. Recorrer el inventario de la tienda seleccionada de
forma secuencial hasta encontrar el código solicitado. Informar al usuario si el producto está disponible o no en el inventario de la tienda. """

def administrar_inventario(inventario):

    
    def buscar_producto(codigo, productos):
        for producto in productos:
            if producto == codigo:
                return True
        return False

    codigo_producto = input("Ingrese el código del producto que está buscando: ")


    print("Seleccione la tienda en la que desea buscar el producto:")
    for tienda in inventario.keys():
        print(tienda)
    tienda_seleccionada = input()

    if tienda_seleccionada in inventario:
        producto_encontrado = buscar_producto(codigo_producto, inventario[tienda_seleccionada])
        if producto_encontrado:
            print("El producto está disponible en el inventario de la tienda.")
        else:
            print("El producto no está disponible en el inventario de la tienda.")
    else:
        print("La tienda seleccionada no existe.")



inventario_sucursal = {
    "sucursal1": ["producto1", "producto2", "producto3"],
    "sucursal2": ["producto4", "producto5", "producto6"],
    "sucursal3": ["producto7", "producto8", "producto9"]
}

administrar_inventario(inventario_sucursal)
