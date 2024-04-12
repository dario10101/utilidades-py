"""
Funciones de orden superior:
Son funciones que reciven como parametro otra funcion

Ej 
filter -> Ayuda a filtrar datos de un iterable
map -> ayuda a convertir datos de un iterable en otros
reduce -> reduce un iterable a un unico valor, ej sumando los items, multiplicandolos, etc.

funcion anonima: 
lambda argumentos : expresion

"""

from functools import reduce


def run():
    print()
    filter_function()
    map_function()
    reduce_function()


"""
Ejemplo: fitrar los numeros impares de una lista, con filter
"""
def filter_function():    
    # primeros 10 numeros naturales:
    my_list = [i for i in range(1,11)]

    # Dejo solo los numeros impares:
    # filter recive una funcion anonima de filtro y un iterable
    # filter retorna un objeto iterable, con 'list' se convierte a lista 
    odd = [list(filter(lambda x: x%2 != 0, my_list))]

    print("filter function: no filter: ", my_list)
    print("filter function: odd numbers: ", odd)
    print()


"""
Ejemplo: convertir una lista de numeros, a sus correspondiantes cuadrados
"""
def map_function():
    # primeros 10 numeros naturales:
    my_list = [i for i in range(1,11)]

    # Creo una lista con los cuadrados de la lista original:
    # map recive una funcion anonima y un iterable
    # map retorna un objeto iterable, con 'list' se convierte a lista 
    squares = [list(map(lambda x: x**2, my_list))]

    print("map function: initial list: ", my_list)
    print("map function: squares: ", squares)
    print()


"""
Ejemplo: multiplicar todos los numeros de una lista
"""
def reduce_function():
    # primeros 5 numeros naturales:
    my_list = [i for i in range(1,6)]

    # reduce recive una funcion anonima y un iterable
    # en la primera iteracion, a es el 1er item y b el 2do, luego, a es el acumulado 
    # y b el siguiente item 
    reduced_list = reduce(lambda a, b: a * b, my_list)

    print("reduce function: initial list: ", my_list)
    print("reduce function: all multiplied: ", reduced_list)
    print()


if __name__ == '__main__':
    run()