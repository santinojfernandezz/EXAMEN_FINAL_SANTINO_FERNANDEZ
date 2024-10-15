from archivos import *
from funciones import *

path = "data_final_20241015.csv"
matriz = cargar_matriz(path)
inicio = True
bandera_matriz_cargada = False
bandera_ingreso_numero = False
opciones = ["carga del archivo", "Ingresar un número entero", "Cuántas secuencias de números consecutivos suman el número ingresado previamente por consola", "secuencia minima de elementos que suman el numero ingresado", "secuencia maxima de elementos que suman el numero ingresado", "salir"]
while inicio:
    menu(opciones)
    opcion = input("Ingrese una opcion:")
    match opcion:
        case "1":
            matriz = cargar_matriz(path)
            bandera_matriz_cargada = True
            
        case "2":
            numero_entero = ingreso_numero()
            bandera_ingreso_numero = True

        case "3":
            if bandera_ingreso_numero and bandera_matriz_cargada:
                busqueda_de_secuencias = suma_secuencias(matriz, numero_entero)
                cantidad = busqueda_de_secuencias["cantidad_de_secuencias"]
                mensaje = f"hubo un total de {cantidad} secuencias que suman {numero_entero}"
                print(mensaje)
            else:
                print("Debes cargar la matriz e ingresar un numero para poder ejecutar la opcion.")
            
        case "4":
            if bandera_ingreso_numero and bandera_matriz_cargada:
                secuencia_de_menos_elementos(matriz, numero_entero)
            else:
                print("Debes cargar la matriz e ingresar un numero para poder ejecutar la opcion.")

        case "5":
            if bandera_ingreso_numero and bandera_matriz_cargada:
                secuencia_de_mas_elementos(matriz,numero_entero)
            else:
                print("Debes cargar la matriz e ingresar un numero para poder ejecutar la opcion.")

        case "6":
            inicio = False
        case _:
            print("Elige una opcion valida")

    print("")

