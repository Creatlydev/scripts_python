class Nodo:

    def __init__(self, data):

        self.item = data
        self.ref = None


class LikenList:

    def __init__(self):

        self.star_nodo = None
        self.count = 0

    def __str__(self):

        if self.star_nodo is None:

            return ("Lista Vacia")

        else:

            n = self.star_nodo
            while n:

                print(n.item, end="  -> " if n.ref else "")
                n = n.ref
            return ""

    def insertStar(self, data):

        new_nodo = Nodo(data)

        new_nodo.ref = self.star_nodo

        self.star_nodo = new_nodo
        self.count += 1

    def insertBefore(self, x, data):

        if self.star_nodo is None:

            print(f" {x!r} no esta en la lista  ")
            return

        if x == self.star_nodo.item:

            new_nodo = Nodo(data)
            new_nodo.ref = self.star_nodo
            self.star_nodo = new_nodo
            self.count += 1

            return

        n = self.star_nodo

        while n.ref is not None:

            if n.ref.item == x:

                break
            n = n.ref

        if n.ref is None:

            print(" Item No Esta en la lista")
            return

        else:

            new_nodo = Nodo(data)
            new_nodo.ref = n.ref
            n.ref = new_nodo
            self.count += 1

    def insertAfter(self, x, data):

        n = self.star_nodo

        while n is not None:

            if n.item == x:
                break

            n = n.ref

        if n is None:
            print("Item no en la lista .")

        else:

            new_nodo = Nodo(data)
            new_nodo.ref = n.ref
            n.ref = new_nodo
            self.count += 1

    def insertpop(self, data):

        new_nodo = Nodo(data)

        if self.star_nodo is None:

            self.star_nodo = new_nodo
            self.count += 1

            return

        n = self.star_nodo

        while n.ref is not None:

            n = n.ref

        n.ref = new_nodo
        self.count += 1

    def insert(self, index, data):

        if index == 1:

            new_nodo = Nodo(data)
            new_nodo.ref = self.star_nodo
            self.star_nodo = new_nodo
            self.count += 1
            return

        if self.star_nodo is not None:

            n = self.star_nodo
            i = 2

            while i < index and n.ref is not None:

                n = n.ref
                i += 1

            if n.ref is None:

                self.inserpop(data)

            else:

                new_nodo = Nodo(data)
                new_nodo.ref = n.ref
                n.ref = new_nodo
                self.count += 1

        else:

            new_nodo = Nodo(data)
            self.star_nodo = new_nodo
            self.count += 1

    def setitem(self, value, new):

        if value == self.star_nodo.item:

            new_nodo = Nodo(new)
            new_nodo.ref = self.star_nodo.ref
            self.star_nodo = new_nodo
            return

        if self.star_nodo is not None:

            n = self.star_nodo

            while n.ref is not None:
                if n.item == value:
                    break

                n = n.ref

            if n.ref is None:

                print("El valor no ha sido encontrado")

            else:

                new_nodo = Nodo(new)
                new_nodo.ref = n.ref.ref
                n.ref = new_nodo

    def delete_star(self):

        if self.star_nodo is not None:
            self.star_nodo = self.star_nodo.ref

            self.count -= 1

    def pop(self):

        if self.star_nodo is not None:
            n = self.star_nodo

            while n.ref.ref is not None:

                n = n.ref

            n.ref = None

            self.count -= 1

    def reversed(self):

        prev = None
        n = self.star_nodo

        while n is not None:
            # print(f"| {")

            next = n.ref
            n.ref = prev
            prev = n
            n = next

        self.star_nodo = prev

    def remove(self, data):

        if self.star_nodo is None:

            print("La Lista esta vacia")
            return

        if self.star_nodo.item == data:

            self.star_nodo = self.star_nodo.ref
            self.count -= 1
            return

        n = self.star_nodo

        while n.ref is not None:

            if n.ref.item == data:
                break

            n = n.ref

        if n.ref is None:

            print("El Elemento no se encontro ...")

        else:

            n.ref = n.ref.ref
            self.count -= 1


a = LikenList()

a.insertpop(1)
a.insertpop(2)
a.insertpop(3)
a.insertpop(4)
a.reversed()


print(a)
