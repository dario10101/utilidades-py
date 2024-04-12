"""
Filtraremos, del archivo DATA los trabajadores que dominan python, los
trabajadores de platzi y las personas ancianas (> 70) usando comprehensions y
funciones de orden superior.

la funcion para crear un diccionario, que es la union de un diccionario y otro
valor, usando el operador | solo funciona a partir de python 3.9. En nuestro caso
se usa para calcular la variable old_people
"""

# Lista de diccionarios de trabajadores
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #filtrar con comprehensions
    filter_with_comprehensions()

    #filtrar con funciones de orden superior
    filter_with_hof()


def filter_with_comprehensions():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults =  [worker["name"] for worker in DATA if worker["age"] > 18]
    #old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]    

    print("\nWITH COMPREHENSIONS: ")
    print_iterable(all_python_devs, "\npython devs: ")
    print_iterable(all_Platzi_workers, "\nplatzi workers: ")
    print_iterable(adults, "\nadult people: ")
    #print_iterable(old_people, "old people: ")


def filter_with_hof():
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))
    
    all_Platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_Platzi_workers = list(map(lambda worker: worker["name"], all_Platzi_workers))

    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    #old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    print("\nWITH HIGH ORDER FUNCTIONS: ")
    print_iterable(all_python_devs, "\npython devs: ")
    print_iterable(all_Platzi_workers, "\nplatzi workers: ")
    print_iterable(adults, "\nadult people: ")
    #print_iterable(old_people, "old people: ")    


def print_iterable(iterable, message):
    print(message)
    for item in iterable:
        print(" - ", item)


if __name__ == '__main__':
    run()