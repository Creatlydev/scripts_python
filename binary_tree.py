

''' creacion de un arbol binario '''


class Nodo:

    def __init__(self, clave, data, rigth=None, left=None, padre=None):

        self.clave = clave
        self.data = data
        self.rigth = rigth
        self.left = left
        self.padre = padre

    def TieneHijoLeft(self):

        return bool(self.left)

    def TieneHijoRigth(self):

        return bool(self.rigth)

    def EsHijoIzquierdo(self):

        return self.padre and self.padre.left == self

    def EsHijoDerecho(self):

        return self.padre and self.padre.rigth == self

    def EsRaiz(self):

        return not self.padre

    def EsHoja(self):

        return not (self.rigth or self.left)

    def TieneAlgunHijo(self):

        return self.rigth or self.left

    def TieneAmbosHijos(self):

        return self.rigth and self.left

    def getLeft(self):

        return self.left

    def getRigth(self):

        return self.rigth

    def getRaiz(self):

        return self.padre

    def changeNodo(self, clave, data, rigth=None, left=None):

        self.clave = clave
        self.data = data
        self.rigth = rigth
        self.left = left

        if self.TieneHijoLeft():

            self.left.padre = self

        if self.TieneHijoRigth():

            self.rigth.padre = self

    def __iter__(self):

        if self:

            if self.TieneHijoLeft():

                for item in self.left:

                    yield item

            yield self.clave

            if self.TieneHijoRigth():

                for item in self.rigth:

                    yield item


''' ----------------------------- '''


class TreeBinary:

    def __init__(self):

        self.raiz = None
        self.size = 0

    def inorden(self, raiz=None):

        if self.raiz != None:

            self.inorden(self.raiz.getLeft())
            print(raiz.getRaiz())
            self.inorden(self.raiz.getRigth())

    def __agregar(self, clave, dato, nodoActual):

        if clave < nodoActual.clave:

            if nodoActual.TieneHijoLeft():

                self.__agregar(clave, dato, nodoActual.left)

            else:

                nodoActual.left = Nodo(clave, dato, padre=nodoActual)

        else:

            if nodoActual.TieneHijoRigth():

                self.__agregar(clave, dato, nodoActual.rigth)

            else:

                nodoActual.rigth = Nodo(clave, dato, padre=nodoActual)

    def agregar(self, clave, dato):

        if self.raiz:
            self.__agregar(clave, dato, self.raiz)

        else:
            self.raiz = Nodo(clave, dato)

        self.size += 1

    def __obtener(self, clave, nodoActual):

        if not (nodoActual):
            return None

        elif nodoActual.clave == clave:
            return nodoActual

        elif clave < nodoActual.clave:
            return self.__obtener(clave, nodoActual.left)

        else:
            return self.__obtener(clave, nodoActual.rigth)

    def get(self, clave):

        if self.raiz:
            conseguir = self.__obtener(clave, self.raiz)
            if conseguir:
                return conseguir

            return None

        return None

    def delNodo(self, clave):

        nodo = self.get(clave)

        if nodo:

            print("ESTA AQUI")

            # OPCION1 -> nodo no tiene hijos
            if not (nodo.TieneAlgunHijo()):

                if nodo.EsHijoIzquierdo():

                    nodo.padre.left = None

                elif nodo.EsHijoDerecho():

                    nodo.padre.rigth = None

                else:

                    self.raiz = None

                return None

            # OPCION2 -> si el nodo tiene un hijo
            if not (nodo.TieneAmbosHijos()):

                if nodo.EsRaiz():

                    self.raiz = nodo.getRigth() or nodo.getLeft()

                elif nodo.EsHijoIzquierdo():

                    if nodo.getLeft():

                        nodo.padre.left = nodo.getLeft()

                    elif nodo.getRigth():

                        nodo.padre.left = nodo.getRigth()

                elif nodo.EsHijoDerecho():

                    if nodo.getLeft():

                        nodo.padre.rigth = nodo.getLeft()

                    elif nodo.getRigth():

                        nodo.padre.rigth = nodo.getRigth()

                return None

            # OPCION3 -> nodo tiene ambos hijos
            if nodo.TieneAmbosHijos():

                minLeft = self.runLeft(nodo.getRigth())
                aux = minLeft.clave
                print(f"AUXILIAR = {aux}")

                self.delNodo(minLeft.clave)

                nodo.clave = aux

                return None

        else:

            print("el Nodo No Existe")

    def runLeft(self, raiz):

        if raiz.getLeft() is not None:

            return self.runLeft(raiz.getLeft())

        return raiz

    def __getitem__(self, clave):
        return self.get(clave)

    def __setitem__(self, clave, value):
        self.agregar(clave, value)


# fuera de la clase .


def inorden(arbol):

    if arbol is not None:

        inorden(arbol.left)

        print(arbol.clave)
        inorden(arbol.rigth)


def preorden(arbol):

    if arbol is not None:

        print(arbol.clave)
        preorden(arbol.left)
        preorden(arbol.rigth)


def postorden(arbol):

    if arbol is not None:

        postorden(arbol.left)
        postorden(arbol.rigth)
        print(arbol.clave)


arbol = TreeBinary()
arbol[10] = "A"
arbol[5] = "B"
arbol[15] = "C"
arbol[3] = "D"
arbol[7] = "E"
arbol[12] = "F"
arbol[20] = "G"


inorden(arbol.raiz)


arbol.delNodo(15)

print()

inorden(arbol.raiz)


'''

		15

				8
			 /     \      raiz = 8
			 7      9     izq = 6
		   /   \  /   \   der = 7
		   6    7 8   11
		 /   \
		3    6

'''

print("Hola Mundo")
