# List comprehensions

# Teniendo los primeros 100 números natulares, crear una lista en donde
# se guarden los números al cuadrado siempre y cuando no sean divisibles entre 3
# cuadrados = []
# for i in range(1,101):
#     if i % 3 != 0:
#         cuadrados.append(i ** 2)

cuadrados = [i**2 for i in range(1,101) if i % 3 != 0]
# lista =  elemento      ciclo            condición
#          a guardar

# 1- Sección que indica el nuevo elemento de lista
# 2- Ciclo a partir del cual se ingresan los valores
# 3- Condición opcional para validar

print(cuadrados)
# Para cada i dentro del rango de 1 a 100, voy aguardar el cuadrado si i no es divisible entre 3

# Ejercicio 
# Crear con list comprehension, una lista de los primeros 1,000 números
# pero solo guarda de todos que son múltiplos de 4,
# que a su vez también sean múltiplos de 6 y de 9