# Obtener un texto ingresado por el usuario y verificar si el texto
# es palíndromo (se escribe igual de izquierda a derecha y viceversa)
# ana
# reconocer
# amor a Roma
texto = input("Dame el texto para analizar si es palíndromo: ")
texto = texto.lower()
texto = texto.strip()
texto_inverso = texto[::-1]
if texto == texto_inverso:
    print("Es palíndromo    ("+texto+" | "+texto_inverso+")")
else:
    print("No es palíndromo    ("+texto+" | "+texto_inverso+")")
