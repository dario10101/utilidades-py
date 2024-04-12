import os

#metodo de inicio de la aplicacion
def iniciarPrograma():
        opcion = 1        
        while opcion != 0:  
                opcion = imprimirMenu()
                ejecutarMenu(opcion)
        fin = input("\nPrograma terminado")

#imprime el menu principal y lee la opcion
def imprimirMenu():    
        os.system("cls")
        print("MENU")
        print("Opcion 1: ")        
        print("Opcion 2: ")        
        print("Opcion 3: ")
        print("Opcion 4: ")
        print("Opcion 0: Salir")
        opcion = ingresarEntero(0,4,"digite opcion(entre 0 y 4): ")
        return opcion	

#ejecuta segun la opcion seleccionada
def ejecutarMenu(opcion):
        if(opcion == 1):
                print("\nOpcion 1:")
        elif(opcion == 2):
                print("\nOpcion 2:")
        elif(opcion == 3):
                print("\nOpcion 3:")
        elif(opcion == 4):
                print("\nOpcion 4:")
        pausa()




def ingresarEntero(mensaje):
        bandera = 0
        valor = 0
        while bandera == 0: 
                try:
                        valor = int(input(mensaje))
                        bandera = 1
                except:
                        print("Error: el dato ingresago debe ser un entero, digitelo nuevamente.")
                        mensaje = "Digite el dato nuevamente: "
        return valor
    


def ingresarEntero(min, max, mensaje):
        bandera = 0
        valor = 0
        while bandera == 0: 
                try:
                        valor = int(input(mensaje))                       
                        bandera = validarRango(min, max, valor)
                except:
                        print("Error: el dato ingresago debe ser un entero, digitelo nuevamente.")
                        mensaje = "Digite el dato nuevamente"
        return valor

def pausa():
        fin = input("\nPresione ENTER para continuar")

def validarRango(min, max, valor):
        if valor <= max and valor >= min:
                return 1
        return 0


iniciarPrograma()
