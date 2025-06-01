from Funciones import *
from Inputs import *
import os

bandera_uno = False
bandera_dos = False
participantes = crear_array(5, "")
puntajes = crear_matriz(5, 3, 0)

while True:
    print("1. Cargar participantes\n2. Cargar puntuciones\n3. Mostrar puntuaciones\n4. Participantes con promedio mayor a cuatro(4)\n5. Participantes con promedio mayor a siete(7)\n6. Promedio de cada jurado\n7. Jurado mas estricto\n8. Buscar participantes por nombre\n9. Top tres(3) participantes con mas puntaje\n10. participantes ordenados alfabeticamente\n11. Salir")
    opcion = pedir_opcion_menu()
    
    if opcion == 1:
        cargar_nombre_participante(participantes)
        bandera_uno = True

    elif opcion == 2 and bandera_uno == True:
        cargar_puntajes(puntajes)
        bandera_dos = True

    elif opcion == 3 and bandera_dos == True:
        mostrar_participantes_con_promedios(participantes, puntajes)
        promedio_general = calcular_promedio_general(puntajes)
        print(f"Promedio general: {promedio_general:.2f}")

    elif opcion == 4 and bandera_dos == True:
        hay_resultados = False
        for i in range(len(participantes)):
            promedio = calcular_promedio_fila(puntajes, i)
            if promedio > 4:
                mostrar_un_participante(participantes, puntajes, i)
                hay_resultados = True
        if not hay_resultados:
            print("No hay participantes con promedio mayor a 4.")

    elif opcion == 5 and bandera_dos == True:
        hay_resultados = False
        for i in range(len(participantes)):
            promedio = calcular_promedio_fila(puntajes, i)
            if promedio > 7:
                mostrar_un_participante(participantes, puntajes, i)
                hay_resultados = True
        if not hay_resultados:
            print("No hay participantes con promedio mayor a 7.")

    elif opcion == 6 and bandera_dos == True:
        for jurado in range(3):
            promedio = calcular_promedio_columna(puntajes, jurado)
            print(f"Promedio del jurado {jurado+1}: {promedio:.2f}")

    elif opcion == 7 and bandera_dos == True:
        promedios = crear_array(3, 0)
        for jurado in range(3):
            promedio = calcular_promedio_columna(puntajes, jurado)
            promedios[jurado] = promedio

        minimo = promedios[0]
        for i in range(1, 3):
            if promedios[i] < minimo:
                minimo = promedios[i]
        print("Jurado/s mas estricto/s: ")
        for i in range(3):
            if promedios[i] == minimo:
                print(f"Jurado {i + 1} con un promedio de {promedios[i]:.2f}")

    elif opcion == 8 and bandera_dos == True:
        nombre_buscado = input("Ingrese el nombre a buscar: ")
        encontrados = False

        for i in range(len(participantes)):
            if participantes[i] == nombre_buscado:
                mostrar_un_participante(participantes, puntajes, i)
                print("")
                encontrados = True

        if not encontrados:
            print("No se encontro participante con ese nombre.")

    elif opcion == 9 and bandera_dos == True:
        ordenar_participantes_por_total(participantes, puntajes)
        print("Top tres participantes con mayor puntaje total:")
        for i in range(3):
            mostrar_un_participante(participantes, puntajes, i)
            print("")
    elif opcion == 10 and bandera_dos == True:
        ordenar_participantes_alfabeticamente(participantes, puntajes)
        mostrar_participantes(participantes, puntajes)

    elif opcion == 11:
        print("Saliendo...")
        break
    input("Toque cualquier boton para continuar...")
    os.system("cls")