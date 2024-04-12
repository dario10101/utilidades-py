""" 
Manejo de excepciones

Una cadena es palindroma si al escribirla al revez, no cambia su valor, por ejemplo:
 - ana
 - abccba
"""

def run():
    string_value = input("Digite una cadena: ")
    
    # Manejo de error de tipo (aunque aqui no va a pasar nada)
    try:
        print("Resultado: ", palindrome(string_value))
    except TypeError as te:
        print("Error de tipo: ", te)


def palindrome(string):
    try:
        if len(string) == 0:
            # Lanzar una excepcion nosotros mismos
            raise ValueError("La cadena no puede ser vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False  
    finally:
        print("funcion palindrome terminada")
          
    

if __name__ == '__main__':
    run()

