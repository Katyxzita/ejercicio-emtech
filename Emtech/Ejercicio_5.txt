venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
costo_Envio = 1500
venta = 0
total_Cajas_Vendidas = 0
venta_Dia = 0
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
    producto = productos_Matriz[1]
    precio = productos_Matriz[2]
    print("El producto es: " + producto)
    print("El precio por caja es: " + str(precio))
    id_Producto = id_Producto+1
    for n in venta_productos:
        if(int(n[0]) == id_Producto):
            cajas_Vendidas  = int(n[1])
            total_Cajas_Vendidas = total_Cajas_Vendidas + cajas_Vendidas
            if (cajas_Vendidas <= 100):
                venta_total_cajas = (cajas_Vendidas * precio + costo_Envio)
            else:
                venta_total_cajas = (cajas_Vendidas * precio) 

if(total_Cajas_Vendidas > 1500):
    print("Aplica descuento del 20%")
else:
    print("No aplica descuento del 20%")
print("El costo total a pagar: " + str(venta_total_cajas))