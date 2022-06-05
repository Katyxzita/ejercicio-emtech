import sys

costo_Envio = 1500
total = 0
productos_Matriz = [[1, "Maiz grano", 285.55], 
        [2,"Pepino",334.72], 
        [3,"Tomate verde",129.00]]
print("Introduzca el id del producto")
id_Producto = int(input())
if(id_Producto > 3):
    print("No existe ese producto")
    sys.exit()
else:
    if (id_Producto >= 1):
        id_Producto = id_Producto-1
    else:
        print("No existe ese producto")
    productos_Matriz = productos_Matriz[id_Producto]
    print("Introduzca la cantidad de cajas a vender")
    cajas_Vender = int(input())
    producto = productos_Matriz[1]
    precio = int(productos_Matriz[2])
    if(cajas_Vender <= 100):
        total = (precio * cajas_Vender + costo_Envio)
        print("La venta es menor o igual a 100 cajas")
        print("Se cobra envio de " + str(costo_Envio))
    else:
        total = (precio * cajas_Vender)
print("El producto es " + producto)
print("El precio es " + str(precio))
print("El total es " + str(total))