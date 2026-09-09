import crud_edades

def leerDatos():
    print("dime la edad:")
    edad = int(input())
    crud_edades.agregar_edad(edad)

    return edad

def menu():
    print("""
    1. Agregar edad
    2. Mostrar edades
    3. Determinar etapa de vida
    4. Mostrar mayor y menor
    0. Salir
    digita una opción valida:
    """)
    opcion = int(input())
    return opcion

def main():
    while True:
        opcion = menu()

        if opcion == 1:
            leerDatos()
        elif opcion == 2:
            print(crud_edades.mostrar())

        elif opcion == 3:
            crud_edades.determinar_etapa_vida()

        elif opcion == 4:
            print(f"el mayor es: {crud_edades.encontrar_mayor()}")
            print(f"el menor es: {crud_edades.encontrar_menor(1)}")

        elif opcion == 0:
            print("Adios...")
            break

        else:
            print("Opción no invalida...")


main()