# Así como en otros lenguajes existe try-catch, aquí es posible utilizar try-except

# Try     - intentará realizar el código que experamos que suceda
# Except  - Si ocurre un error dentro del bloque try, aquí se concentrará y se ejecutará el código de este bloque
# Else    - este se ejecuta solo si no hubo ninguna excepción dentro del try
# Finally - Se ejecuta siempre al final, se haya lanzado una excepción o no


# Existen distintos tipos de excepciones como TypeError o ValueError y se pueden guardar dentro de una variable

# Hay formas de generar errores condicionados y esto es elevando una excepción con RAISE, que indica el tipo 
# de error y el mensaje

def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False 


def run():
    try:
        print(palindrome(1))
    except TypeError:
        print("Solo se puede agregar strings")


if __name__ == '__main__':
    run()