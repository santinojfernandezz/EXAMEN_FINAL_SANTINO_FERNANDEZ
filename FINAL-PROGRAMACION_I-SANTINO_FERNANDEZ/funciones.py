
def ingreso_numero()-> int:
    """Esta funcion pide un numero por consola y valida que realmente sea un numero y que sea de uno, dos o tres digitos
    Returns:
        numero_validado(int): devuelve el numero ya validado
    """
    numero = input("ingrese un numero: ")

    while not numero.isdigit() or len(numero) > 3 or len(numero) < 1:
        numero = input("Ingrese un NUMERO, porfavor: ")

    numero_validado = int(numero)
    
    return numero_validado

def menu(opciones: list):
    """muestra el menu con las opciones
        Args:
        opciones (lista): lista de opciones que van a ser mostradas en consola
    """
    for opcion in range(len(opciones)):
        print(f"{opcion + 1}) {opciones[opcion].capitalize()}")

def buscar_secuencias_horizontales(matriz: list)->list:
    """esta funcion busca de manera horizontal las secuencias de numeros
    que se encuentras en la matriz

    Args:
        matriz (list): matriz de los numeros donde se buscaran las secuencias

    Returns:
        list: lista de las secuenias encontradas
    """
    secuencias = []
    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[0])
    bandera = False
    secuencia_actual = []
    for i in range(cantidad_filas):
        for j in range(cantidad_columnas - 1):
            if matriz[i][j] + 1 == matriz[i][j + 1]:
                if not bandera:
                    secuencia_actual = [matriz[i][j], matriz[i][j + 1]]
                    bandera = True
                else:
                    secuencia_actual.append(matriz[i][j+1])
            else:
                if len(secuencia_actual) > 1:
                    secuencias.append(secuencia_actual)
                bandera = False
                secuencia_actual = []
    return secuencias

def suma_secuencias(matriz: list, numero_entero: int)->dict:
    """esta funcion llama a la funcion -buscar_secuencias_horizontales-, y con las secuencias que devuelve esta funcion
    suma los elementos de estas y ve si su suma da el numero ingresado.

    Args:
        matriz (list): matriz de los numeros donde se buscaran las secuencias
        numero_entero (int): numero ingresado por consola que se comparara con la suma de las secuencias.

    Returns:
        dict: diccionario que devuelve las secuencias que suman al numero ingreado(con la key -secuencias-) y 
        la cantidad de secuencias que suman al numero ingresado(con la key -cantidad_de_secuencias-).
    """
    secuencias = buscar_secuencias_horizontales(matriz)
    secuencias_suman_al_ingresado = []
    contador_secuencias = 0
    suma = 0
    for secuencia in secuencias:
        for i in secuencia:
            suma += i
        if suma == numero_entero:
            contador_secuencias +=1
            secuencias_suman_al_ingresado.append(secuencia)
        suma = 0

    retorno = {"secuencias": secuencias_suman_al_ingresado,
               "cantidad_de_secuencias": contador_secuencias}
    return retorno

def secuencia_de_menos_elementos(matriz: list, numero: int)->dict:
    """llama a la funcion -suma_secuencias- y mediante el informe que esta funcion devuelve encuentra
    la secuencia minima que sus elementos sumados dan el numero ingresado. y posteriormente lo printea con un
    mensaje.

    Args:
        matriz (list): matriz de los numeros donde se buscaran las secuencias
        numero (int): numero ingresado por consola que se comparara con la suma de las secuencias.
    """
    informe_secuencias = suma_secuencias(matriz, numero)
    secuencias = informe_secuencias["secuencias"]
    if informe_secuencias["cantidad_de_secuencias"] == 1:
        mensaje = f"la secuencia minima que sumando sus elementos da el num: {numero}, es {secuencias}"
    elif informe_secuencias["cantidad_de_secuencias"] > 1:
        bandera = True
        secuencia_min = None
        cantidad_de_elementos_min = 0
        for i in secuencias:
            if bandera:
                cantidad_de_elementos_min = len(i)
                secuencia_min = i
                bandera = False
            else:
                if len(i) < cantidad_de_elementos_min:
                    cantidad_de_elementos_min = len(i)
                    secuencia_min = i
        mensaje = f"la secuencia minima que sumando sus elementos da el num: {numero}, es {secuencia_min}"
    else:
        mensaje = f"no hay secuencias que sumando elementos den el num: {numero}"
    print(mensaje)

def secuencia_de_mas_elementos(matriz: list, numero: int):
    """llama a la funcion -suma_secuencias- y mediante el informe que esta funcion devuelve encuentra
    la secuencia maxima que sus elementos sumados dan el numero ingresado. y posteriormente lo printea con un
    mensaje.

    Args:
        matriz (list): matriz de los numeros donde se buscaran las secuencias
        numero (int): numero ingresado por consola que se comparara con la suma de las secuencias.
    """
    informe_secuencias = suma_secuencias(matriz, numero)
    secuencias = informe_secuencias["secuencias"]
    if informe_secuencias["cantidad_de_secuencias"] == 1:
        mensaje = f"la secuencia minima que sumando sus elementos da el num: {numero}, es {secuencias}"
    elif informe_secuencias["cantidad_de_secuencias"] > 1:
        bandera = True
        secuencia_max = None
        cantidad_de_elementos_max = 0
        for i in secuencias:
            if bandera:
                cantidad_de_elementos_max = len(i)
                secuencia_max = i
                bandera = False
            else:
                if len(i) > cantidad_de_elementos_max:
                    cantidad_de_elementos_max = len(i)
                    secuencia_max = i

        mensaje = f"la secuencia minima que sumando sus elementos da el num: {numero}, es {secuencia_max}"
    else:
        mensaje = f"no hay secuencias que sumando elementos den el num: {numero}"
    print(mensaje)



