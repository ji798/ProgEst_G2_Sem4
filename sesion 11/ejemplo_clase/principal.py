import crud

def leerDatos():
    print("dime la nota:")
    nota = int(input())
    crud.agregar_nota(nota)

    return nota

def menu():
    print("""
    1. Agregar nota
    2. Mostrar notas
    3. Evaluar notas
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
            print(crud.mostrar())

        elif opcion == 3:
            crud.evaluarNotas()

        elif opcion == 0:
            print("Adios...")
            break

        else:
            print("Opción no invalida...")


main()