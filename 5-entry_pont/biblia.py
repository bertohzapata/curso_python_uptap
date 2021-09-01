def bienvenida():
    print(""" Bienvenido
                Esta librería te permite conocer 
                entre otras cosas como leer pasajes de la biblia.""")

def valor_name():
    print(__name__)

def como_leer():
    print(""" ¿Que es la biblia?
La biblia es el primer libro escrito por la humanidad, tiene millones de años, y en ella se encuentran los principios básicos de la vida y de la sociedad por eso es muy importante tenerlo en cuenta para muchas religiones que profesan su forma de ver la vida por medio de la biblia, practicando los conceptos que en ella están escritos a través de parábolas o de oraciones.

¿Como se debe buscar en la biblia?
Puede parecer simple, pero no lo es porque hay que tener en cuenta que la biblia es un conjunto de libros canónicos del judaísmo y también del cristianismo, y la canonicidad de cada uno de esos libros va variando dependiendo de la tradición que se adopte.

La biblia es el libro mas vendido del mundo y ha sido traducido en mas de 2000 idiomas, es el único libro que transmite la palabra de Dios.

Formas de buscar en la biblia
Lo esencial es saber que la biblia se encuentra dividida en capítulos y en versículos.
En el texto de la biblia los capítulos están indicados con números grandes  y los versículos al contrario, están indicados con números pequeños.

2. La cita del texto bíblico nos brinda la siguiente información

El nombre del libro bíblico
El capitulo correspondiente
Los versículos que deben ser.
Si tenemos en cuenta estos tres aspectos es mas facil encontrar el texto que estemos buscando en la biblia.

3.  En este punto les mostraremos un ejemplo para que puedan guiarse mucho mejor.

MC- Libro de Marcos
1- Capitulo 1
30-35 versículo del 30 al 35.
4.Los guiones cortos indican las secuencia de los versículos, la coma es la encargada de separar los capítulos de los versículos y el punto es la abreviatura del libro.

En la biblia se pueden encontrar diferentes tipos de símbolos como por ejemplo:

AM. que significa libro de amos

8. Capitulo 8

4-9.10-14 significa que se debe leer los capitulos del al 4 al 9  y del 10 al numero 14.

5. Si cuando estamos buscando en la biblia nos encontramos con una sigla «ss» significa que a partir de ese versiculo se deben leer todos los siguientes.

7.El guion mas largo Mt. 5–7 se encarga de indicar una serie de capitulos en este caso particular del libro de Mateo, y segun los numeros se deben leer desde el primer numero marcado y los siguientes hasta el ultimo numero, en este caso seria del cinco al siete. """)
def menu():
    print(""" 
        1- ¿Cómo leer?
        2- Buscar
    """)


def buscar(libro, capitulo, versiculo_inicial = 0, versiculo_final = 0):
    busqueda = f'{libro} {str(capitulo)}'
    if versiculo_inicial > 0: busqueda += f':{str(versiculo_inicial)}'
    if versiculo_final > 0: busqueda += f'-{str(versiculo_final)}'
    print("=>Tu búsqueda es:", busqueda)
    # text_db = busqueda_db(libro, capitulo, versiculo_inicial, versiculo_final)
    # return text_db




if __name__ == '__main__':
    bienvenida()
    valor_name()