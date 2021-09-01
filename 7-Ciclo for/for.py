
# for i in range(0,10):
#     print(i)


# for i in range(10):
#     print(i)


# palabra = 'Humberto'
# for i in palabra:
#     print(i)


numero = int(input("Dame un número: "))
cadena_numeros = ""
if numero > 0:
    for i in range(0,numero):
        cadena_numeros += (str(i) + ",")
    cadena_numeros += str(numero)
else:
    print('Número no aceptado')
