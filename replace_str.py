
''' reemplaza cadena '''


import re
import string


def funcion(x):

    letras = string.ascii_letters

    lista = x.split()

    mover = [lista[i][1:] + lista[i][0]+"ay" if lista[i][0]
             in letras else lista[i] for i in range(len(lista))]

    print(" ".join(mover))


funcion("hola mundo Oye H")


def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)


print(pig_it("Hola_mundo oye k"))


def pig_it(text):

    return __import__("re").sub(r'\b\w+\b', lambda m: m.group(0)[1:] + m.group(0)[0] + 'ay', text)
