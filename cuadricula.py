#Escribir una función que dibuje una cuadrícula como la siguiente:
#La función debe recibir un parámetro que indique la cantidad de cuadrados a imprimir, y otro
#parámetro que indique la cantidad de columnas de cada cuadrado. En la figura de ejemplo, esos
#parámetros serían 2 y 4.

def cuadricula (cuadrados, columnas):
    borde_superior = ("+----" * columnas) + "+"
    borde_lateral = ("|    " * columnas) + "|"
    
    for f in range (cuadrados):
        print (borde_superior)
        for _ in range (3):
            print(borde_lateral)
    print (borde_superior)

cuadrados = 4
columnas = 2
cuadricula (cuadrados, columnas)