# import primer_modulo
import biblia

def run():
    biblia.menu()
    opcion = int(input())
    if opcion == 1:
        biblia.como_leer()
    elif opcion == 2:
        libro = input("Libro: ")
        cap = int(input("Capítulo: "))
        v1 = int(input("Versículo inicial: "))
        v2 = int(input("Versículo final: "))
        biblia.buscar(libro,cap,v1,v2)
    else:
        print("Lo siento, no reconozco esa opción")


if __name__ == '__main__':
    run()