import os
FILE_PATH = os.path.dirname(__file__)

def read():
    numbers = []
    with open(f"{FILE_PATH}/archivos/numbers.txt", "r", encoding="utf-8") as f:
        [numbers.append(int(line)) for line in f]
    print(numbers)


def write():
    names = ["Humberto", "Edlin", "Kevin", "Antonio", "Alfredo", "Paulina"]
    with open(f"{FILE_PATH}/archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    # write()


if __name__ == '__main__':
    run()