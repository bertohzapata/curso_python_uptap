# Reglas:
# Correr el programa un que se muestren con guiones bajos los espacios de la palabra que se siente que adivinar.
# El programa no se detendrá hasta haber adivinado las palabras
# Si una letra no coincide, volver a preguntar la palabra
# Cada vez que se se digite una nueva palabra limpiar la consola y mostrar los guiones bajos y letras según avance el juego


# Se debe incorporar comprehensions, manejo de errores y manejo de archivos.
# Utiliza el archivo data.txt y léelo para obtener las palabras
import os
import random
import unicodedata
FILE_PATH = os.path.dirname(__file__)

def obtener_palabra():
    palabras = []
    with open(f"{FILE_PATH}/data.txt", "r", encoding="utf-8") as file:
        [palabras.append(str(line.rstrip('\n'))) for line in file]
        return palabras


def normalizar_palabra(palabra):
    palabra = ''.join(c for c in unicodedata.normalize('NFKD', palabra) if unicodedata.category(c) != 'Mn')
    return palabra.upper()


def preparar_juego(palabra):
    dic_palabra = []
    for letra in palabra:
        dic = {}
        dic['letra'] = letra
        dic['adivinada'] = False
        dic_palabra.append(dic)
    return dic_palabra


def imprimir_juego(lista_palabra):
    for dic_palabra in lista_palabra:
        if dic_palabra['adivinada']:
            print(dic_palabra['letra'], end=' ')
        else:
            print('_', end=' ')
    print('\n')


def validar_letra(letra):
    if letra.isnumeric():
        raise ValueError("No se admiten numeros")
    if len(letra) > 1:
        raise ValueError("No se admite mas de un caracter")


def intento_adivinanza(letra, lista_palabra):
    os.system("cls")
    palabra_adivinada = True
    for dic_palabra in lista_palabra:
        if dic_palabra['letra'] == letra:
            dic_palabra['adivinada'] = True
    

    for dic_palabra in lista_palabra:
        if dic_palabra['adivinada'] == False:
            palabra_adivinada = False
            break

    return palabra_adivinada


def run():
    #Limpiando la consola 
    os.system('cls')
    # Seleccionar palabra
    palabras = obtener_palabra()
    palabra = random.choice(palabras)

    # Normalizando palabra
    palabra = normalizar_palabra(palabra)
    
    # Preparando palabra para juego (devuelve una lista de diciconarios)
    palabra_juego = preparar_juego(palabra)

    # Menú juego
    adivinada = False
    while(adivinada == False):
        try:
            print("¡Adivina la palabra!\n")
            imprimir_juego(palabra_juego)
            nueva_letra = input("Ingresa una letra: ")
            validar_letra(nueva_letra)
            nueva_letra = normalizar_palabra(nueva_letra)
            # Adivinar
            adivinada = intento_adivinanza(nueva_letra, palabra_juego)
        except ValueError as ve:
            os.system("cls")
            print(ve)
    
        
    print("¡Juego finalizado!\n")
    imprimir_juego(palabra_juego)




if __name__ == '__main__':
    run()