from Funciones import *

#ESPECIFICA
def pedir_opcion_menu() -> int:
    """ Valida que el numero ingresado este entre 1 y 11


    Returns:
        int: El numero a usar en el menu
    """
    while True:
        entrada = input("Su opción: ")
        if validar_entero_positivo(entrada):
            numero = int(entrada)
            if 1 <= numero <= 11:
                return numero
            else:
                print("Error: ingrese un numero entre 1 y 11.")
        else:
            print("Error: ingrese un numero entero positivo. Intente nuevamente.")



#ESPECIFICA
def cargar_nombre_participante(array_participantes:list) -> None:
    """ Se encarga de cargar los nombres de los participantes ingresados por el usuario

    Args:
        array_participantes (list): Agrega los nombres al array de participantes
    """
    for i in range(len(array_participantes)):
        while True:
            nombre = input(f"Ingrese el nombre del participante {i + 1}: ")
            if es_nombre_valido(nombre):
                array_participantes[i] = nombre
                break
            else:
                print("Error: el nombre solo puede tener letras y espacios, y no puede estar vacio.")

#ESPECIFICA
def cargar_puntajes(matriz_puntajes: list) -> None:
    """
    Carga los puntajes del jurado para cada participante, validando que sean enteros entre 1 y 10.

    Args:
        matriz_puntajes (list): Matriz de 5x3 donde se guardan los puntajes.
    """
    for fil in range(len(matriz_puntajes)):
        for col in range(len(matriz_puntajes[fil])):
            while True:
                entrada = input(f"Ingrese puntaje del jurado {col+1} para el participante {fil+1}: ")
                if validar_entero_positivo(entrada):
                    numero = int(entrada)
                    if numero >= 1 and numero <= 10:
                        matriz_puntajes[fil][col] = numero
                        break
                    else:
                        print("Error: el puntaje debe estar entre 1 y 10.")
                else:
                    print("Error: debe ingresar un numero entero positivo.")