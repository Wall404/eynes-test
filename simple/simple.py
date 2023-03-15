import random

LONGITUD = 10


def generarLista():
    lista = [dict(zip([i], [random.randint(1, 100)]))
             for i in range(1, LONGITUD)]
    return lista


lista = generarLista()

print(lista)
