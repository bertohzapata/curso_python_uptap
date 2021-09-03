# Desarolla una herramienta generadora de contraseñas aleatoreas a partir de una serie de
# listas de números, letras mayúsculas, letras minúsculas y caracteres especiales.
# El tamaño de la contraseña debe ser de 15 caracteres y cada vez que se ejecute el programa.
# este arrojará una nueva contraseña aleatoria
# EJ1. Tu contraseña es: r5A*4LUO!@mg1("
# EJ2. Tu contraseña es:  CqnSazzqE,_<sNk"
# EJ3. Tu contraseña es: >~&oL{7F3DiRñAZ"

# Requisitos del ejercicio: Utilizar los conceptos vistos hasta ahora:
#   - Ciclos
#   - Listas o tuplas
#   - Random
#   - Entry point
#   - Funciones

# PISTA:  SIMBOLOS = ('*', '+', '-', '/', '@',)



import random

def random_char(BASE):
    return random.choice(BASE)
    

def run():
    pass
    MAYUSCULAS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
    MINISCULAS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    SIMBOLOS = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')
    NUMEROS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

    BASE = MAYUSCULAS + MINISCULAS + SIMBOLOS + NUMEROS
    contraseña = []
    for i in range (15):
        contraseña.append(random_char(BASE))
    contraseña = ''.join(contraseña)
    print(contraseña)


if __name__ == '__main__':
    run()

