# 1- menu de opciones para la entrada por teclado
# 2- operaciones aritméticas básicas dependiendo de cada opción
# 3- imprimiendo valores dependiendo de la opción del menú
def solicitar_numero(n):
    return int(input("Número " + str(n) + ": ")) 

def suma(numero1, numero2):
    print("Resultado:",(numero1 + numero2))

def resta(numero1, numero2):
    print("Resultado:",(numero1 - numero2))

def mult(numero1, numero2):
    print("Resultado:",(numero1 * numero2))

def div(numero1, numero2):
    print("Resultado:",(numero1 / numero2))

def div_int(numero1, numero2):
    print("Resultado:",(numero1 // numero2))

def potencia(numero1, numero2):
    print("Resultado:",(numero1 ** numero2))

def mod(numero1, numero2):
    print("Resultado:",(numero1 % numero2))

opcion = int(input(""" ==== Calculadora básica ====
    1- sumar
    2- restar
    3- multiplicar
    4- dividir (decimal)
    5- division entera
    6- potencia
    7- modulo

    => Opción elegida: """))

if opcion == 1:
    n1 = solicitar_numero(1)
    n2 = solicitar_numero(2)
    suma(n1,n2)
elif opcion == 2:
    n1 = solicitar_numero(1)
    n2 = solicitar_numero(2)
    resta(n1,n2)
elif opcion == 3:
    n1 = solicitar_numero(1)
    n2 = solicitar_numero(2)
    mult(n1,n2)
elif opcion == 4:
    n1 = solicitar_numero(1)
    n2 = solicitar_numero(2)
    div(n1,n2)
elif opcion == 5:
    n1 = solicitar_numero(1)
    n2 = solicitar_numero(2)
    div_int(n1,n2)
elif opcion == 6:
    n1 = solicitar_numero(1)
    n2 = solicitar_numero(2)
    potencia(n1,n2)
elif opcion == 7:
    n1 = solicitar_numero(1)
    n2 = solicitar_numero(2)
    mod(n1,n2)
