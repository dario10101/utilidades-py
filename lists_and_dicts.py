"""
Manejo de listas y diccionarios, un diccionario puede contener listas
y viseversa, una lista puede contener diccionarios

"""

def run():
    print_lists_and_dicts()  


def print_lists_and_dicts():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {"firstname" : "Ruben", "lastname": "Dorado"}
    print(my_list)
    print(my_dict)
    print("my format: ", my_dict["firstname"], "-", my_dict["lastname"])

    # Lista de diccionarios
    super_list = [
        {"firstname" : "Ruben", "lastname": "Cordoba"},
        {"firstname" : "Dario", "lastname": "Dorado"},
        {"firstname" : "Dario", "lastname": "Cordoba"},
    ]

    # Diccionario de listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43],
    }

    # Imprimir diccionario de listas
    for key, value in super_dict.items():
        print(key, "-", value)

    # Imprimir lista de diccionarios
    for item in super_list:
        print(item["firstname"], "-", item["lastname"])


if __name__ == '__main__':
    run()