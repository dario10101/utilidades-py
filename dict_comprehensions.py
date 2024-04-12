"""
dictionary comprenhensions es una estructura de python que sirve para crear nuevos diccionarios
Estructura: {key: value for element in iterable if condicion}
el if es opcional

"""

def run():
    # Calcular cubos, Metodo largo
    print("by long method: ", create_cubes_long_method(10))
    print()

    # Calcular cubos, Usando comprehensions
    print("by short method: ", create_cubes_short_method(10))


"""
Crea una lista de los n primeros cubos (n incluido), de la forma larga, divisibles entre 5
"""
def create_cubes_long_method(count):
    cubes = {}
    for i in range(1, count+1):
        if i % 5 == 0:
            cubes[i] = i ** 3

    return cubes


"""
Crea una lista de los n primeros cubos (n incluido) usando dict comprehensions, divisibles entre 5
"""
def create_cubes_short_method(count):
    cubes = {i: i ** 3 for i in range (1, count+1) if i % 5 == 0}
    return cubes


if __name__ == '__main__':
    run()