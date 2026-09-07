def calcular_pago(horas, tarifa):
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)


calcular_pago(40, 120)

# La siguiente instrucción produciría NameError:
# print(pago)

"""Si, el print(pago) da error porque la variable pago solo existe dentro de la función calcular_pago, 
es decir, tiene un alcance local. Por lo tanto, no se puede acceder a ella desde fuera de la función."""