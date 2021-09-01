# def nombre_funcion(parámetros):
    # sentencias


# def saludo(nombre):
#     print("Hola ", nombre)


# nombre = input("Nombre: ")
# saludo(nombre)



# def operacion(numero1, numero2):
#     # resultado = numero1 + numero2
#     # return resultado
#     return numero1 + numero2


# n1 = int(input("Dame un númmero: "))
# n2 = int(input("Dame un númmero: "))
# resultado = operacion(n1, n2)
# print("Tu resultado es:", resultado)


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


n = int(input(""" Verificador de numeros pares:
                    Número: """))
numero_par = es_par(n)
if numero_par:
    print("Tu número es par")
else:
    print("Tu número es impar")
