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
    """función pendiente"""
    print("funcion pendiente.")


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
                c1 = float(input("Ingrese la primera calificación: "))
                c2 = float(input("Ingrese la segunda calificación: "))
                c3 = float(input("Ingrese la tercera calificación: "))

                promedio = calcular_promedio(c1, c2, c3)

                print("El resultado del promedio es:", promedio)
                evaluar_desempeno(promedio)

            case "2":
                generar_reporte(None)

            case "3":
                print("Saliendo del programa...")
                continuar = False

            case _:
                print("ingrese una opción valida")


main()