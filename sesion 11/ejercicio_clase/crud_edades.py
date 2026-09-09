#Registro de estudiantes
"""
Registrar edades de n cantidad de estudiantes
"""

edades = []

def agregar_edad(edad):
    edades.append(edad)

def mostrar():
    return edades

def determinar_etapa_vida():
    for edad in edades:
        if not isinstance(edad, int) or edad < 0:
            print(f"{edad}, no es una edad válida.")
            continue
        else:
            if edad < 12:
                print(f"{edad}, es un niño.")

            elif edad >= 12 and edad < 18:
                print(f"{edad}, es un adolescente.")

            elif edad >= 18 and edad < 60:
                print(f"{edad}, es un adulto.")

            else:
                print(f"{edad}, es un adulto mayor.")

def encontrar_mayor():
    if edades:
        mayor = max(edades)
        return mayor
    else:
        print("No hay edades registradas.")

def encontrar_menor():
    if edades:
        menor = min(edades)
        return menor
    else:
        print("No hay edades registradas.")