import os
from datetime import datetime, date, timedelta
from random import randint

def manejoVector():
        #creacion:
        vector = []
        
        vectorAux = [10, 5, "hola"]
        vector.append(vectorAux)

        vectorAux2 = [4,7]
        vector.append(vectorAux2)
        
        longitud = len(vector)

        for i in range(0,longitud):
                print(vector[i])

        print("Longitud: " + str(longitud))

def manejoFecha():
        #AÑO-MES-DIA
        fechaHoy = datetime.now().date()
        print(fechaHoy)
        
        fechaHoy = str(fechaHoy)
        print(fechaHoy)
        
        fechaHoy = fechaHoy.split("-")
        print(fechaHoy)

#leer y validar un numero entero desde teclado
def ingresarEntero(min, max, mensaje):
        bandera = 0
        valor = 0
        while bandera == 0: 
                try:
                        valor = int(input(mensaje))                       
                        bandera = validarRango(min, max, valor)
                except:
                        print("Error: el dato ingresago debe ser un entero, digitelo nuevamente.")
                        mensaje = "Digite el dato nuevamente: "
        return valor

#leer y validar un numero entero desde teclado
def ingresarEnteroSinRango(mensaje):
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

#ingresar fecha asegurandose que sea en el futuro
def ingresarFechaFutura():
        bandera = 0
        while bandera == 0:
                dia = ingresarEntero(1,31,"Digite dia: ")
                mes = ingresarEntero(1,12,"Digite mes: ")
                año = ingresarEntero(2018,3000,"Digite año: ")
                bandera = validarFechaFutura(dia,mes,año)
                if bandera == 0:
                        print("Fecha incorrcta.")
                
        fecha = convertirFechaAStrAMD(dia,mes,año)
        return fecha

#ingresar fecha cualquiera
def ingresarFecha():
        bandera = 0
        while bandera == 0:
                dia = ingresarEntero(1,31,"Digite dia: ")
                mes = ingresarEntero(1,12,"Digite mes: ")
                año = ingresarEnteroSinRango("Digite año: ")
                bandera = validarFecha(dia,mes,año)
                if bandera == 0:
                        print("Fecha incorrecta.")
                
        fecha = convertirFechaAStrAMD(dia,mes,año)
        return fecha

#valida el rango de un numero entero
def validarRango(min, max, valor):
        if valor <= max and valor >= min:
                return 1
        return 0

#valida que una fecha sea valida y no haya pasado
def validarFechaFutura(dia, mes, año):        
        #primero, miro si la fecha es valida
        resultado = validarFecha(dia,mes,año)

        if(resultado == 1):
                fecha = datetime.now().date()
                fecha_dada = datetime(año, mes, dia)
                fecha_final = fecha_dada.strftime('%Y-%m-%d')

                if str(fecha_final) < str(fecha):                       
                        return 0
                else:
                        return 1

        return resultado        

#verifica si una fecha es valida
def validarFecha(dia,mes,año):
        resultado = 0
        if(dia > 0 and dia < 32 and mes > 0 and mes < 13):
                resultado = 1
                if(mes == 2): #febrero 28 0 29 depende si es bisciesto
                        bis = bisciesto(año)
                        if(bis == 1):
                                if(dia > 29):
                                        resultado = 0
                        else:
                                if(dia > 28):
                                        resultado = 0                         
                if(mes == 4 or mes == 6 or mes == 9 or mes == 11): #meses de maximo 30 dias
                        if(dia >= 31):
                                resultado = 0
        return resultado

#verifica si un año es bisciesto
def bisciesto(año):
        if(año % 4 == 0):
                if(año % 100 != 0):
                        return 1
                else:
                        if(año % 400 == 0):
                                return 1                        
        return 0

#convierte los atributos de dia, mes, año en una cadena (año-mes-dia)
def convertirFechaAStrAMD(dia,mes,año):
        return (str(año) + "-" + str(mes) + "-" + str(dia))

def convertirStrAFechaAMD(strFecha):
        fecha = strFecha.split("-")
        fecha[0] = int(fecha[0])
        fecha[1] = int(fecha[1])
        fecha[2] = int(fecha[2])
        return fecha
        

#pausa en la consola
def pausa():
        fin = input("\nPresione ENTER para continuar")

#valida si un numero es par
def esPar(num):
        if(num % 2) == 0:
                return 1
        return 0

#numero aeatorio
def numRandom(min,max):
        return randint(min,max)

def ordenamientoBurbuja(lista,tam):
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lista[j] > lista[j+1]):
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k;

#porcentaje de valor en total
def porcentajeDe(valor, total):
        return ((valor * 100) / (total))

#sacar un porcentaje de total
def porcentaje(porc, total):
        return ((porc * total) / 100)
        



        


        
        


