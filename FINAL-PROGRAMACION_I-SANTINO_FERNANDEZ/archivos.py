def cargar_matriz(path:str):
    """funcion que carga la matriz recibida 

    Args:
        path (str): path de la matriz para extraerla 

    Returns:
        list: matriz ya extraida
    """
    matriz = []
    with open(path, "r") as archivo:
        filas = archivo.readlines()
        for fila in filas:
            fila = fila.split(";")
            largo = len(fila)
            fila[largo - 1] = fila[largo - 1].strip("\n")
            for i in range(len(fila)):
                fila[i] = int(fila[i])
            matriz.append(fila)
    print("MATRIZ CARGADA")
    return matriz
