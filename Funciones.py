
#GENERAL
def validar_entero_positivo(cadena:str) -> bool:
    """ Valida que la cadena sea un entero positivo

    Args:
        cadena (str): La cadena a validar

    Returns:
        bool: Retorna true si es entero positivo, retorna False si la cadena no lo es
    """
    if len(cadena) == 0:
        return False
    for caracter in cadena:
        if ord(caracter) < 48 or ord(caracter) > 57:
            return False
    return True

#GENERAL
def crear_array(cantidad_elementos:int,valor_inicial:any) -> list:
    """ Se encarga de crear un array

    Args:
        cantidad_elementos (int): La cantidad de elementos del array
        valor_inicial (any): Con que valor se pone cada elemento del array

    Returns:
        list: Retoran el array creado
    """
    array = [valor_inicial] * cantidad_elementos
    return array

#ESPECIFICA
def es_nombre_valido(cadena: str) -> bool:
    """
    Valida que el nombre tenga al menos 3 letras(En mayusculas o minusculas), y permite espacios

    Args:
        cadena (str): Nombre a validar

    Returns:
        bool: True si es valido, False si contiene caracteres no permitidos o tiene menos de 3 letras
    """
    if len(cadena) == 0:
        return False

    contador_letras = 0

    for caracter in cadena:
        codigo = ord(caracter)
        if (65 <= codigo <= 90) or (97 <= codigo <= 122):
            contador_letras += 1
        elif codigo != 32:
            return False
    if contador_letras >= 3:
        return True
    else:
        return False
    
#GENERAL
def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    """ Crea una matriz con las dimenciones dadas

    Args:
        cantidad_filas (int): Cantidad de filas
        cantidad_columnas (int): Cantidad de columnas
        valor_inicial (any): Valor de cada elemento

    Returns:
        list: Retorna la matriz creada como lista
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        #matriz.append(fila)
        matriz += [fila]
        
    return matriz

#GENERAL
def validar_estructura(array: list, matriz: list, indice: int) -> bool:
    """
    Valida que el array y la matriz no sean listas vacias,
    que el indice sea valido.

    Args:
        array (list): lista
        matriz (list): matriz
        indice (int): Posicion a validar

    Returns:
        bool: True si todo es valido, False si hay algun error.
    """
    if type(array) != list or type(matriz) != list:
        print("Error: las estructuras deben ser listas.")
        return False

    if len(array) == 0 or len(matriz) == 0:
        print("Error: las estructuras no pueden estar vacias.")
        return False

    if indice < 0 or indice >= len(array):
        print("Error: indice fuera de rango en el array.")
        return False

    if indice >= len(matriz):
        print("Error: el indice no coincide con la cantidad de filas en la matriz.")
        return False

    return True

# GENERAL
def calcular_promedio_general(matriz: list) -> float:
    """
    Calcula el promedio general de todos los valores en la matriz.

    Args:
        matriz (list): Matriz

    Returns:
        float: Promedio general de todos los elementos.
    """
    suma_total = 0
    cantidad_total = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma_total += matriz[i][j]
            cantidad_total += 1

    promedio = suma_total / cantidad_total
    return promedio

# ESPECIFICA
def mostrar_un_participante(participantes: list, puntajes: list, indice: int) -> None:
    """
    Muestra el nombre de un participante, su puntaje individual y su promedio.

    Args:
        participantes (list): Lista de los nombres de los participantes.
        puntajes (list): Matriz que contiene los puntajes.
        indice (int): Posicion del participante a mostrar.

    Returns:
        None
    """
    if not validar_estructura(participantes, puntajes, indice):
        return

    print(f"Nombre: {participantes[indice]}")
    fila = puntajes[indice]
    for i in range(len(fila)):
        print(f"Puntaje Jurado {i+1}: {fila[i]}")

#ESPECIFICA
def mostrar_participantes(participantes: list, puntajes: list) -> None:
    """
    Muestra todos los participantes con sus puntajes.
    """
    for i in range(len(participantes)):
        mostrar_un_participante(participantes, puntajes, i)
        print("")

#ESPECIFICA
def mostrar_participantes_con_promedios(participantes: list, puntajes: list) -> None:
    """Muestra los participantes con su promedio individuales

    Args:
        participantes (list): Array
        puntajes (list): Matriz
    """
    for i in range(len(participantes)):
        mostrar_un_participante(participantes, puntajes, i)
        promedio = calcular_promedio_fila(puntajes, i)
        print(f"Promedio individual: {promedio:.2f}")
        print("")

#GENERAL
def calcular_promedio_fila(matriz: list, fila: int) -> float:
    """
    Calcula el promedio de una fila de una matriz.

    Args:
        matriz (list): Matriz
        fila (int): fila a procesar.

    Returns:
        float: Promedio de la fila.
    """
    suma = 0
    cantidad_columnas = len(matriz[fila])

    for col in range(cantidad_columnas):
        suma += matriz[fila][col]

    promedio = suma / cantidad_columnas
    return promedio

# GENERAL
def calcular_promedio_columna(matriz: list, columna: int) -> float:
    """
    Calcula el promedio de una columna de la matriz.

    Args:
        matriz (list): Matriz.
        columna (int): columna a procesar.

    Returns:
        float: Promedio de la columna.
    """
    suma = 0
    cantidad_filas = len(matriz)

    for fil in range(cantidad_filas):
        suma += matriz[fil][columna]

    promedio = suma / cantidad_filas
    return promedio

# ESPECIFICA
def ordenar_participantes_por_total(participantes: list, puntajes: list) -> None:
    """ Ordena los participantes de mayor a menor

    Args:
        participantes (list): lista de participantes
        puntajes (list): Matriz de puntajes
    """
    for izq in range(len(puntajes) - 1):
        for der in range(izq + 1, len(puntajes)):
            suma_izq = sumar_fila(puntajes, izq)
            suma_der = sumar_fila(puntajes, der)
            if suma_izq < suma_der:
                intercambiar_elementos(participantes, izq, der)
                intercambiar_elementos(puntajes, izq, der)

# GENERAL
def sumar_fila(matriz: list, fila: int) -> int:
    """
    Suma los elementos de una fila de la matriz.

    Args:
        matriz (list): Matriz.
        fila (int): fila a sumar.

    Returns:
        int: Suma total de la fila.
    """
    suma = 0
    for col in range(len(matriz[fila])):
        suma += matriz[fila][col]
    return suma

#GENERAL
def intercambiar_elementos(array:list,izq:int,der:int) -> None:
    """ Intercambia los elementos a ordenar.

    Args:
        array (list): Lista a ordenar.
        izq (int): Posicion primer elemento.
        der (int): Posicion segundo elemento.
    """
    auxiliar = array[izq]
    array[izq] = array[der]
    array[der] = auxiliar

#ESPECIFICA
def ordenar_participantes_alfabeticamente(participantes: list, puntajes: list) -> None:
    """Ordena los participantes alfabeticamente, lo puntajes tambien los ordena

    Args:
        participantes (list): array de los participantes
        puntajes (list): matriz de puntajes
    """
    for izq in range(len(participantes) - 1):
        for der in range(izq + 1, len(participantes)):
            if participantes[izq] > participantes[der]:
                intercambiar_elementos(participantes, izq, der)
                intercambiar_elementos(puntajes, izq, der)