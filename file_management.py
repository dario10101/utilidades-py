
from os import remove
from os import mkdir
import os.path as path


class FileManager:
    """Funciones utiles para el manejo de archivos en python"""

    #def __init__(self, path = None):
    #    self.path = path


    def create_directory(self, directory):
        """
        Crea una nueva carpeta en la ubicacion de la clase 
        (verificar los atributos del metodo mkdir para especificar ubicacion)

        Attributes:
            directorio -- nombre de la carpeta
        """
        try:
            mkdir(directory)
        except OSError as os_error:
            print(os_error)
        else:
            print("Se ha creado el directorio: %s " % directory)


    def delete(self, base_name):
        """
        elimina un archivo especificado

        Attributes:
            base_name -- ruta del archivo
        """ 
        try:      
            if path.exists(base_name):
                remove(base_name)
            return True
        except PermissionError as pe:
            print(pe)
            return False


    def read(self):
        numbers = []
        
        # Esta sentencia with impide que el archivo se dañe en caso de que ocurra un problema
        # utf-8 impide errores de caracteres extraños
        # r: solo lectura
        with open("./files/numbers.txt", "r", encoding="utf-8") as f:
            for line in f:
                numbers.append(int(line))
        print(numbers)


    def write(self):
        names = ["Rubén", "Dario", "Ana", "Juana", "Saul"]

        # Esta sentencia with impide que el archivo se dañe en caso de que ocurra un problema
        # utf-8 impide errores de caracteres extraños (ej la tilde de Rubén)
        # w: sobreescritura, a: concatenar
        with open("./files/names.txt", "w", encoding = "utf-8") as f:
            for name in names:
                f.write(name)
                f.write("\n")


    def write_new_line(self, base_name, content_items, separator=","):
        """ 
        Escribe una linea en un archivo, de la forma: 
        1,2,3
        a partir de un arreglo

        Attributes:
            base_name -- Ruta del archivo, si no existe, lo crea automaticamente
            content_items -- Iterable que contiene items que van en la linea a escribir
            separator -- separador de cada item del iterable (, por defecto)
        """
        try:
            with open(base_name, 'a') as f:        
                f.write(separator.join([str(c) for c in content_items]) + "\n")
        except TypeError as te:
            print("> ", te)
                

def run():
    file_tools = FileManager()
    
    file_tools.create_directory("test")
    file_tools.delete("test")
    file_tools.write_new_line("files/1.txt", None)
    file_tools.write_new_line(None, [1,2,3], "-")
    file_tools.write_new_line("./files/1.txt", [1,2,3], "-")

    file_tools.read()
    file_tools.write()

    print("finished successfull")


if __name__ == '__main__':
    run()