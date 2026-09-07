nombre_producto1 = "Camiseta"
precio_producto1 = 600.0
cantidad_producto1 = 3

nombre_producto2 = "Pantalón"
precio_producto2 = 700.0
cantidad_producto2 = 5

def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

def calcular_descuento(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.08
    return 0

def calcular_iva(monto):
    return monto * 0.15

def mostrar_resumen(nombre_producto, precio, cantidad):
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal)
    monto_con_descuento = subtotal - descuento
    iva = calcular_iva(monto_con_descuento)
    total = monto_con_descuento + iva

    print(f"--- RESUMEN DE VENTA: {nombre_producto} ---")
    print("Precio unitario: C$", round(precio, 2))
    print("Cantidad: ", cantidad)
    print("Subtotal: C$", round(subtotal, 2))
    print("Descuento: C$", round(descuento, 2))
    print("IVA: C$", round(iva, 2))
    print("Total: C$", round(total, 2))

mostrar_resumen(nombre_producto1, precio_producto1, cantidad_producto1)
print("\n")

mostrar_resumen(nombre_producto2, precio_producto2, cantidad_producto2)

