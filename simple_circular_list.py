

class Nodo:

    def __init__(self, data):

        self.data = data
        self.next = None
        self.values = []


class ListCircSimple:

    def __init__(self):

        self.start = None
        self.end = None
        self.size = 0

    def run(self):

        aux = self.start

        while aux:

            print(aux.data, end=" - ")
            aux = aux.next

            if aux == self.start:
                break

    def add_first(self, data):

        new_nodo = Nodo(data)

        if self.start is None:

            self.start = self.end = new_nodo
            self.end.next = self.start

        else:

            new_nodo.next = self.start
            self.start = new_nodo
            self.end.next = self.start

        self.size += 1

    def append(self, data):

        new_nodo = Nodo(data)

        if self.start is None:

            self.start = self.end = new_nodo
            self.end.next = self.start

        else:

            aux = self.end
            new_nodo.next = self.start
            self.end = new_nodo
            aux.next = new_nodo

        self.size += 1

    def insert(self, index, data):

        new_nodo = Nodo(data)

        if self.start is None:

            self.start = self.end = new_nodo
            self.end = self.start

        elif index == 0:

            new_nodo.next = self.start
            self.start = new_nodo
            self.end.next = self.start

        elif index >= self.size:

            aux = self.end
            new_nodo.next = self.start
            self.end = aux.next = new_nodo

        else:

            aux = self.start
            i = 1

            while aux.next:

                if i == index:

                    break

                aux = aux.next
                i += 1

            new_nodo.next = aux.next
            aux.next = new_nodo

        self.size += 1

    def setitem(self, index, data):

        if self.start is None:

            print("La Lista Esta Vacia")

        elif index == 0:

            new_nodo = Nodo(data)

            if self.size == 1:

                self.start = self.end = new_nodo
                self.end.next = self.start

            else:

                new_nodo.next = self.start.next
                self.start = new_nodo
                self.end.next = self.start

        elif index >= self.size:

            print("El Index ha excedido el rango de la lista")

        else:

            aux = self.start
            i = 1

            while aux.next:

                if i == index:

                    break

                aux = aux.next
                i += 1

            new_nodo = Nodo(data)
            new_nodo.next = aux.next.next
            aux.next = new_nodo

    def pop_first(self):

        if self.start is None:

            print("La Lista Esta Vacia")
            return None

        elif self.start.next == self.start:

            self.start = self.end = None

        else:

            self.start = self.start.next
            self.end.next = self.start

        self.size -= 1

    def pop(self):

        if self.start is None:

            print("La Lista Esta Vacia")
            return None

        elif self.start == self.start.next:

            self.start = self.end = None

        else:

            aux = self.start

            while aux.next.next != self.start:

                aux = aux.next

            aux.next = self.start
            self.end = aux

        self.size -= 1

    def remove(self, data):

        if self.start is None:

            print("La Lista Esta Vacia")
            return None

        elif self.size == 1:

            if self.start.data == data:

                self.start = self.end = None

            else:

                print("No Se Encontro El Elemento")
                return None

        elif self.start.data == data:

            self.start = self.start.next
            self.end.next = self.start

        elif self.end.data == data:

            self.pop()

        else:

            aux = self.start

            while aux.next != self.start:

                if aux.next.data == data:

                    break

                aux = aux.next

            if aux.next == self.start:

                print("El Item No Se Encontro")
                return None

            else:

                aux.next = aux.next.next

        self.size -= 1

    def reversed(self):

        prev = self.end
        aux = self.end = self.start

        i = 0

        while i != self.size:

            next = aux.next
            aux.next = prev
            prev = aux
            aux = next
            i += 1

        self.start = prev

    def __setitem__(self, index, value):

        self.setitem(index, value)

    def __len__(self):

        return self.size


lista = ListCircSimple()

lista.add_first(1)
lista.add_first(2)
lista.add_first(3)
lista.add_first(4)
lista.add_first(5)

lista.reversed()

lista.run()
