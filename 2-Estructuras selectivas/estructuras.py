numero = input (""" Si me das un número te diré si:
            - Es menor a cero
            - Es cero
            - Es mayor a cero
             """)

numero = int(numero)

if numero < 0:
    print("Tu número es menor a 0")
elif numero == 0:
    print("Tu número es cero")
else:
    print("Tu número es mayor a 0")

