"""
Me falto integrar len, suma y metodos de listas.
No lo pude integrar porque no le encontre un lugar especifico donde se  pudiera usar en mi programa
https://github.com/A01715836/Proyecto_TC1038
"""



def calcular_promedio(calificacion1, calificacion2, calificacion3):
    """función que calcula el promedio de las calificaciones"""
    return (calificacion1 + calificacion2 + calificacion3) / 3


def evaluar_desempeno(promedio):
    """función que evalúa el desempeño"""
    if promedio >= 9:
        print("Excelente")
    elif promedio >= 8:
        print("Muy bien")
    elif promedio >= 7:
        print("Trata de mejorar")
    else:
        print("Reprobado")


def generar_reporte(datos):
    for fila in datos:
        print(fila)
    

matriz = []

def main():
    """menu de la calculadora"""
    continuar = True

    while continuar:
        print("MENÚ DE GESTION ACADEMICA")
        print("1. Calcular promedio y evaluar estudiante")
        print("2. Generar reporte (función pendiente)")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        match opcion:
            case "1":
                nombres = []
                calificaciones = []
                for i in range(5):
                    persona = input("ingrese su nombre: ")
                    persona = persona.upper()
                    c1 = float(input("Ingrese la primera calificación: "))
                    c2 = float(input("Ingrese la segunda calificación: "))
                    c3 = float(input("Ingrese la tercera calificación: "))

                    promedio = calcular_promedio(c1, c2, c3)
                    nombres.append(persona)
                    calificaciones.append([c1, c2, c3])
                    string = ",".join(nombres)
                    print("nombre:",nombres)
                    print("el resultado del promedio es:", promedio)
                    print("estudiantes registrados:",texto)
                    evaluar_desempeno(promedio)
                    matriz.append([persona, c1, c2, c3])
                

            case "2":
                generar_reporte(matriz)

            case "3":
                print("adios")
                continuar = False

            case _:
                print("ingrese una opción valida")


main()