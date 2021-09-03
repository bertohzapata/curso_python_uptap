# Crea un diccionario donde las llaves sean los primeros 100 números naturales que no sean
# divisibles entre 3
#  y cuyos valores sean esos mismos pero elevados al cubo

diccionario_cubo = {}
# for i in range(1,101):
#     if i % 3 != 0:
#         diccionario_cubo[i] = i**3

diccionario_cubo = {i : i**3 for i in range(1,101) if i % 3 != 0}
# elemento a guardar ___ : ___  ciclo   condición
print(diccionario_cubo)