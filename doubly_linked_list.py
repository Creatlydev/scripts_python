
import time


class Nodo:

    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None


class ListDobleEnlaze:

    def __init__(self):

        self.start = None
        self.end = None
        self.size = 0

    # metodo que recorre la lista del inicio al final

    def __str__(self):

        aux = self.start

        while aux:

            print(aux.data, end=" ->")
            aux = aux.next

        return ""

    # metodo que recorre del final al inicio

    def run_reverse(self):

        aux = self.end

        while aux:

            print(aux.data, end=" ->")

            aux = aux.prev

    # metodo que agrega un data al inicio de la lista

    def append_first(self, data):

        if self.start is None:

            new_nodo = Nodo(data)
            self.start = self.end = new_nodo

        else:

            new_nodo = Nodo(data)

            new_nodo.next = self.start
            self.start.prev = new_nodo
            self.start = new_nodo

        self.size += 1

    # metodo que agrega un data al final de la lista

    def append(self, data):

        if self.start is None:

            self.start = self.end = Nodo(data)

        else:

            new_nodo = Nodo(data)
            aux = self.end
            new_nodo.prev = self.end

            self.end = aux.next = new_nodo

        self.size += 1

    # metodo que reemplaza el valor del index pasado por el parametro newvalue

    def setitem(self, index, newvalue) -> None:

        if self.start is None:

            print("La Lista Esta Vacia")

        elif index == 0:

            new_nodo = Nodo(newvalue)
            new_nodo.next = self.start.next
            self.start.next.prev = new_nodo
            self.start = new_nodo

        elif index == self.size - 1:

            new_nodo = Nodo(newvalue)
            new_nodo.prev = self.end.prev
            self.end.prev.next = new_nodo
            self.end = new_nodo

        elif index >= self.size:

            print("Error : el index pasado excedio el rango de la lista")

        else:

            aux = self.start
            i = 1

            while aux.next is not None:

                if i == index:

                    break

                aux = aux.next
                i += 1

            new_nodo = Nodo(newvalue)
            aux.next.next.prev = new_nodo
            new_nodo.next = aux.next.next
            new_nodo.prev = aux
            aux.next = new_nodo

    # metodo que inserta un valor en en el index pasado

    def insert(self, index, value):

        if self.start is None:

            self.start = self.end = Nodo(value)
            self.size += 1

        elif index == 0:

            new_nodo = Nodo(value)
            new_nodo.next = self.start
            self.start.prev = new_nodo
            self.start = new_nodo
            self.size += 1

        elif index >= self.size:

            new_nodo = Nodo(value)
            aux = self.end
            new_nodo.prev = self.end

            self.end = aux.next = new_nodo
            self.size += 1

        else:

            new_nodo = Nodo(value)

            aux = self.start
            indx = 1

            while aux.next is not None:

                if indx == index:

                    break

                aux = aux.next
                indx += 1

            aux.next.prev = new_nodo
            new_nodo.next = aux.next
            new_nodo.prev = aux

            aux.next = new_nodo

            self.size += 1

    # metodo que elimina el elemento final de la lista

    def pop(self):

        if self.start is None:

            print("Lista Vacia")

        elif self.size == 1:

            self.star = self.end = None
            self.size -= 1

        else:

            self.end.prev.next = None
            self.end = self.end.prev
            self.size -= 1

    # metodo que elimina el primer elemento de la lista

    def del_first(self):

        if self.start is None:

            print("No Hay Elementos")

        elif self.start.next is None:

            self.start = self.end = None
            self.size -= 1

        else:

            self.start.next.prev = None

            self.start = self.start.next
            self.size -= 1

    # metodo que elimina el item en cualquier parte de la lista

    def remove(self, item):

        if self.start is None:

            print("No Hay Elementos")

        elif self.start.data == item:

            self.start.next.prev = None

            self.start = self.start.next
            self.size -= 1

        elif self.end.data == item:

            self.end.prev.next = None
            self.end = self.end.prev
            self.size -= 1

        else:

            aux = self.start

            while aux.next:

                if aux.next.data == item:

                    break

                aux = aux.next

            if aux.next is None:

                print("El Item No Esta En La Lista")

            else:

                aux.next.next.prev = aux
                aux.next = aux.next.next
                self.size -= 1

    # metodo que revierte la lista

    def reversed(self):

        aux = self.end = self.start

        prev = None

        while aux:

            next = aux.next
            aux.next = prev
            aux.prev = next
            prev = aux
            aux = next

        self.start = prev

    # metodo que sobrecarga osea es igual a lista[index] = value 		 solo hace la llamada el metodo setitem que hace el trabajo

    def __setitem__(self, index, value):

        self.setitem(index, value)


lista = ListDobleEnlaze()

lista.append(10)
lista.append(20)
lista.append(30)
lista.append(40)
lista.append(50)
