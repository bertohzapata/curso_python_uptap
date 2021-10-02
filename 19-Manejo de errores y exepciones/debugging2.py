def divisors(num):
    try:
        if num < 0:
            raise ValueError("No se admiten números negativos")
        else:
            divisors = []
            for i in range(1, num + 1):
                if num % i == 0:
                    divisors.append(i)
            return divisors
    except ValueError as ve:
        print(ve)
        return False



def run():
    valor_erroneo = True
    while(valor_erroneo):
        try:
            num = int(input("Ingresa un numero: "))
            print(divisors(num))
            valor_erroneo = False
            print("Termino el programa")
        except ValueError:
            print("Debes ingresar un número")


if __name__ == "__main__":
    run()