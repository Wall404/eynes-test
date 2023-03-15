import random

LONGITUD = 10


def generarLista():
    return [dict(zip([i], [random.randint(1, 100)]))
            for i in range(1, LONGITUD)]


lista = generarLista()

print(lista)
