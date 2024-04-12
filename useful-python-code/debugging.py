"""
Calculo de los divisores de un numero

"""

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        print("divisores: ", divisors(num))
        print("Terminó mi programa")
    except:
        print("no se pudo calcular el palindromo")


if __name__ == '__main__':
    run()