

class Nodo:

    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None


class ListCircDoble:

    def __init__(self):

        self.start = None
        self.end = None
        self.size = 0

    def run(self):

        aux = self.start

        while aux:

            next = aux.next

            print(aux.data, end=" -> " if next != self.start else "")
            aux = next

            if aux == self.start:
                break

        print()

    def runBack(self):

        aux = self.end

        while aux:

            prev = aux.prev

            print(aux.data, end=" -> " if prev != self.end else "")

            aux = prev

            if aux == self.end:
                break

        print()

    # agregar al inicio de la lista

    def add_first(self, data):

        new_nodo = Nodo(data)

        if self.start is None:

            self.start = self.end = new_nodo
            self.start.prev = self.end
            self.end.next = self.start

        else:

            new_nodo.next = self.start
            self.start.prev = new_nodo
            self.start = new_nodo
            self.start.prev = self.end
            self.end.next = self.start

        self.size += 1

    # agregar al final de la lista

    def append(self, data):

        new_nodo = Nodo(data)

        if self.start is None:

            self.start = self.end = new_nodo
            self.end.next = self.start
            self.start.prev = self.end

        else:

            new_nodo.prev = self.end
            new_nodo.next = self.start
            self.end.next = new_nodo
            self.end = new_nodo
            self.start.prev = self.end

        self.size += 1

    # inserta un elemento en el index pasado como arguemnto si este excede el rango de la lista se agrega al final de la lista

    def insert(self, index, data):

        new_nodo = Nodo(data)

        if self.start is None:

            self.start = self.end = new_nodo
            self.start.prev = self.end
            self.end.next = self.start

        elif index == 0:

            new_nodo.next = self.start
            self.start.prev = new_nodo
            self.start = new_nodo
            self.start.prev = self.end
            self.end.next = self.start

        elif self.size <= index:

            new_nodo.prev = self.end
            new_nodo.next = self.start
            self.end.next = new_nodo
            self.end = new_nodo
            self.start.prev = self.end

        elif self.size - 1 == index:

            new_nodo.prev = self.end.prev
            new_nodo.next = self.end
            self.end.prev.next = new_nodo
            self.end.prev = new_nodo

            # 2 3 8 4

        else:

            aux = self.start
            i = 1

            while aux.next != self.start:

                if i == index:
                    break

                aux = aux.next
                i += 1

            new_nodo.next = aux.next
            new_nodo.prev = aux
            aux.next = new_nodo

        self.size += 1

    # cambia el valor del posicion de lista pasada al parametro index con el valor del parametro data

    def setitem(self, index, data):

        new_nodo = Nodo(data)

        if self.start is None:

            print("La Lista Esta Vacia")
            return None

        elif index == 0:

            if self.size == 1:

                self.start = self.end = new_nodo
                self.start.prev = self.end
                self.end.next = self.start

            else:

                new_nodo.next = self.start.next
                self.start.next.prev = new_nodo

                self.start = new_nodo
                self.end.next = self.start
                self.start.prev = self.end

        elif index >= self.size:

            print("El Index Paso el rango de la lista")
            return None

        elif index == self.size - 1:

            new_nodo.prev = self.end.prev
            self.end.prev.next = new_nodo
            self.end = new_nodo
            self.end.next = self.start
            self.start.prev = self.end

        else:

            aux = self.start
            i = 1

            while aux.next != self.start:

                if index == i:
                    break

                aux = aux.next
                i += 1

            new_nodo.next = aux.next.next
            aux.next.next.prev = new_nodo
            new_nodo.prev = aux
            aux.next = new_nodo

    # metodo que elimina el primer elemento de la lista

    def pop_first(self):

        if self.start is None:

            print("La Lista Esta Vacia")
            return None

        elif self.size == 1:

            self.start = self.end = None

        else:

            self.start = self.start.next
            self.start.prev = self.end
            self.end.next = self.start

        self.size -= 1

    # metodo que elimina el ultimo elemento de la lista

    def pop(self):

        if self.start is None:

            print("La Lista Esta Vacia")
            return None

        elif self.size == 1:

            self.start = self.end = None

        else:

            self.end = self.end.prev
            self.start.prev = self.end
            self.end.next = self.start

        self.size -= 1

    # metodo que borra el argumento pasado al parametro value en cualquier parte de la lista

    def remove(self, value):

        if self.start is None:

            print("La Lista Esta Vacia")
            return None

        elif self.size == 1:

            if self.start.data == value:

                self.start = self.end = None

            else:

                print("El Item No Esta En La Lista")
                return None

        elif self.start.data == value:

            self.start = self.start.next
            self.start.prev = self.end
            self.end.next = self.start

        elif self.end.data == value:

            self.end = self.end.prev
            self.start.prev = self.end
            self.end.next = self.start

        else:

            aux = self.start

            while (aux.next != self.start):

                if aux.next.data == value:
                    break

                aux = aux.next

            if (aux.next == self.start):

                print("El Elemento No Se Encontro")
                return None

            else:

                aux.next.next.prev = aux
                aux.next = aux.next.next

            self.size -= 1

    def reverse(self):

        prev = self.end
        aux = self.end = self.start
        i = 0

        while i != self.size:

            next = aux.next
            aux.next = prev
            aux.prev = next
            prev = aux
            aux = next
            i += 1

        self.start = prev

    # _____

    def __setitem__(self, index, value):

        self.setitem(index, value)

    def __len__(self):

        return self.size


''' ----------------------------- '''


lista = ListCircDoble()

lista.add_first(5)
lista.add_first(4)
lista.add_first(3)
lista.add_first(2)
lista.add_first(1)
lista.append(6)

lista.reverse()

lista.run()

print()

lista.runBack()
