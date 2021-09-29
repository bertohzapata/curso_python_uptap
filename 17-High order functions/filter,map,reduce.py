# Una función de order superior es una función que recibe como parámetro otra función

# def saludo(func):
#     func()

# def hola():
#     print('Hola!!!')

# def adios():
#     print("Adios!!!")


# saludo(hola)
# saludo(adios)



# ================ FILTER ================
#       Con list comprehension
# list= [1,4,5,6,9,13,19,21]

# odd = [i for i in list if i % 2 != 0]

# print(odd)

#       Con filtro
# my_list = [1,4,5,6,9,13,19,21]
# odd = list(filter(lambda x: x%2 != 0, my_list))
# print(odd)



# ================ MAP ================
#       Con list comprehension
# list2 = [1,2,3,4,5]
# squares = [i**2 for i in list2]
# print(squares)

#       Con map
# my_list2 = [1,2,3,4,5]
# squares = list(map(lambda x: x**2, my_list2))
# print(squares)



# ================ REDUCE ================
#       Con for
# list3 = [2, 2, 2, 2, 2]
# all_mutiplied = 1
# for i in list3:
#     all_mutiplied = all_mutiplied * i

# print(all_mutiplied)


#       Con reduce
from functools import reduce
my_list3 = [2, 2, 2, 2, 2]
all_multiplied = reduce(lambda a,b: a* b, my_list3)
print(all_multiplied)