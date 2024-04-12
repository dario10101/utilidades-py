"""
list comprenhensions es una estructura de python que sirve para crear nuevas listas
Estructura: [element for element in iterable if condicion]
el if es opcional

"""

def run():
    # Calcular cuadrados, Metodo largo
    print("by long method: ", create_squares_long_method(10))

    # Calcular cuadrados, Usando comprehensions
    print("by short method: ", create_squares_short_method(10))

    # Multipos de 4, 6 y 9 usando list comprehensions, hasta n_multiples
    n_multiples = 1000
    print("multiples of 4, 6 and 9: ", calculate_multiples([4, 6, 9], n_multiples))


"""
Crea una lista de los n primeros cuadrados (n incluido), de la forma larga, si son divisibles entre 3
"""
def create_squares_long_method(count):
    squares = []
    for i in range(1, count+1):
        if i % 3 == 0:
            squares.append(i ** 2)

    return squares


"""
Crea una lista de los n primeros cuadrados (n incluido), si son divisibles entre 3, 
usando list comprehensions
"""
def create_squares_short_method(count):
    squares = [i ** 2 for i in range (1, count+1) if i % 3 == 0]
    return squares


"""
Calcula los multiplos especificados en una lista, para los primeros n numeros naturales (n incluido)
"""
def calculate_multiples(list_restrictions, count):
    numbers = [i for i in range(1, count+1) if is_multiple(i, list_restrictions)]
    return numbers


"""
Valida si un numero es multiplo de todos los items de una lista
"""
def is_multiple(number, restrictions):
    for restriction in restrictions:
        if number % restriction != 0:
            return False
    return True


if __name__ == '__main__':
    run()