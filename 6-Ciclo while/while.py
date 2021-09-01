# contador = 0

# while contador < 10:
#     print(contador + 1)
#     contador += 1

# Desarrolla un programa que pida al usuario un número
# entero postivo y muestre en pantalla la cuenta atrás desde ese número
# hastra el cero. Cada número debe ir separado por una coma
numero = int(input("Dame un número: "))
cadena_numeros = ""
if numero > 0:
    while(numero != 0):
        cadena_numeros += (str(numero) + ",")
        numero -= 1
    cadena_numeros += str(numero)
else:
    print('Número no aceptado')

print(cadena_numeros)