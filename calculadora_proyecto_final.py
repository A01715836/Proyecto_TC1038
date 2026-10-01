
#https://github.com/A01715836/A01715836_avance-proyecto
# función que calcula el promedio de las calificaciones
def calcular_promedio(calif1, calif2, calif3):
    return (calif1 + calif2 + calif3) / 3

# función que evalúa el desempeño 
def evaluar_desempeno(promedio):
    if promedio >= 9:
        print("Excelente")
    elif promedio >= 8:
        print("Muy bien")
    elif promedio >= 7.9:
        print("Trata de mejorar")
    else:
        print("Reprobado")

# función pendiente
def generar_reporte(datos):
    print("funcion pendiente.")

#menu de la calculadora 
def main():
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

                # Cálculo de promedio
                promedio = calcular_promedio(c1, c2, c3)
                
                print("El resultado del promedio es:", promedio)
                evaluar_desempeno(promedio)

            case "2":
                # función pendiente
                generar_reporte(None)

            case "3":
                print("Saliendo del programa...")
                continuar = False

            case _:
                print("ingrese una opción valida")

main()
