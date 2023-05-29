
''' desarrollo de tres en raya con el Paradigma POO '''

import os
import random
from time import sleep
from draw_board import tablero_per as tablero
from copy import deepcopy


def LOGO(can):

    logo = f'''
                     _______----_______
                    |{can:^18}|
                    |        En        |
                    |_______RAYA_______|
		
	'''
    return logo


''' funcion que devuelve la magnitud del tablero '''


def magnitud():

    logo = LOGO("----")

    can = {"1": "Tres", "2": "Cuatro", "3": "Cinco"}

    a1, a2, a3 = "Tres En Raya", "Cuatro En Raya", "Cinco En Raya"

    entry = "Cual Es Tu Opcion ."
    error = "Elige 1 - 2 o 3 por favor"
    again = "|Enter| para intentar otra vez"

    while True:
        os.system("cls")
        # print("\033[2J\033[0;1f")

        print(f"{logo}")

        print(f"{'1':>15} →  {a1} .")
        print(f"{'2':>15} →  {a2} .")
        print(f"{'3':>15} →  {a3} .")

        print()

        opcion = input(f"{entry:>{14+len(entry)}} →  ")

        if opcion in ("1", "2", "3"):
            return can[opcion]

        print(f"\n{error:^59}\n")
        input(f"{again:>{14+len(again)}} ")


''' funcion que devuelve cuantos jugadores seran uno o dos y tambien tiene la opcion a escoger de ver la simulacion del juegos entre dos maquinas que hacen movimientos con inteligencia artificial basica '''


def juegan(can) -> str:

    __LOGO__ = LOGO(can)

    a, b, c = "1 Jugador", "2 Jugadores", "Juego De Maquinas"
    giones = "-"*26
    entra = "Cual Es Tu Opcion →  "
    error = "Elige (a - b o c) |Enter| Para intentar otra vez"
    can = "cuatro"

    while True:

        os.system("cls")

        print(f"{__LOGO__}")

        print(f"{'a':>15} →  {a}")
        print(f"{'b':>15} →  {b}")
        print(f"{'c':>15} →  {c}")

        print()

        print(f"{giones:>40}")
        print()

        opcion = input(f"{entra:>34}").lower()

        if (opcion in ("a", "b", "c")):

            return opcion

        input(f"\n{error:^59}")


# Clase Principal Del Juego
''' ----- Inicio De La Clase ---- '''


class EnRaya():

    global can

    # metodo construtor

    def __init__(self, opcion):

        self.opcion = opcion
        self.LOGO = LOGO(can)
        self.tablero = lambda x: [[" " for i in range(x)] for i in range(x)]

        if can == "Tres":
            self.tablero = self.tablero(3)

        elif can == "Cuatro":
            self.tablero = self.tablero(4)

        else:
            self.tablero = self.tablero(5)

    ''' metodo que rellena el tablero de la posicion 
	f = fila  r = columna 
	con el parametro ficha '''

    def rellenar_tablero(self, f, r, ficha):

        self.tablero[f][r] = ficha

    '''metodo que se encarga de determinar la fila y columna dado el numero de casilla
                escogido por el usuario'''

    def determinar_casilla(self, numero):

        if numero % len(self.tablero) != 0:
            fila = numero // len(self.tablero)

        else:
            fila = (numero // len(self.tablero)) - 1

        columna = numero - (fila * len(self.tablero))
        columna -= 1
        return [fila, columna]

    ''' metodo que se encarga de obtener los indices de la casilla donde el jugador desea realizar el movimiento '''

    def escoge_casilla(self, name):

        validas = list(range(len(self.tablero)**2))

        casilla = f"Escoge Una Casilla 1 - {len(validas)} "

        error1 = "Digita El Numero De La Casilla"
        error2 = "Escoge Una Casilla Dentro Del Rango"
        error3 = "esta casilla ya esta ocupada"

        print()

        turn = f"Es Tu Turno {name}"
        print(f"{turn:^59}")

        print()
        casilla = input(f"{casilla:>{14+len(casilla)}} →  ")

        if not (casilla.isdigit()):

            print(f'\n{error1:^59}')
            return None

        elif not (int(casilla) - 1 in validas):

            print(f"\n{error2:^59}")
            return None

        fila, columna = self.determinar_casilla(int(casilla))

        if self.tablero[int(fila)][int(columna)] != " ":

            print(f"\n{error3:^59}")
            return None

        else:
            return [fila, columna]

    ''' metodo que comprueba si hay un ganador o sea un fila o columna o diagonal del tablero tienen una misma ficha '''

    def hay_ganador(self, ta, ficha):

        rayas = []

        for i in ta:

            rayas.append(i)

        columnas = []
        for i in range(len(self.tablero)):
            columnas.append([])

            for j in range(len(self.tablero)):

                columnas[i].append(ta[j][i])

        for i in columnas:

            rayas.append(i)

        diagonales = [[], []]
        for i in range(len(self.tablero)):

            diagonales[0].append(ta[i][i])
            diagonales[1].append(ta[i][-i-1])

        for i in diagonales:
            rayas.append(i)

        for i in rayas:

            if not (" " in i):

                if len(i) == i.count(ficha):
                    return True

            else:

                pass

        return False

    ''' comprueba si el en el tablero aun quedas casillas por rellenar de ser asi devuelve false , en caso contrario devuelve True pues signifia que si no ha visto ganador hasta el momento es un empate '''

    def hay_empate(self):

        if not (any([" " in i for i in self.tablero])):
            return True

        return False

    ''' metodo que devuelve los indices del tablero que el pc escoge inteligentemente mediante bucles for primera revisa si tiene opcion a ganar de no ser asi pasa comprobar si hay opcion de bloquear una juegada de lo contrario escoge una de las casillas vacias al azar '''

    def mueve_pc(self, youficha, otherficha):

        copia = deepcopy(self.tablero)

        for i in range(len(copia)):

            for j in range(len(copia)):

                if copia[i][j] == " ":
                    copia[i][j] = youficha

                    if self.hay_ganador(copia, youficha):
                        return [i, j]

                    copia[i][j] = " "

        for i in range(len(copia)):

            for j in range(len(copia)):

                if copia[i][j] == " ":

                    copia[i][j] = otherficha

                    if self.hay_ganador(copia, otherficha):
                        return [i, j]

                    copia[i][j] = " "

        long = len(self.tablero)

        vacias = [[i, j] for i in range(long) for j in range(
            long) if self.tablero[i][j] == " "]

        coords = random.choice(vacias)
        return coords

    ''' metodo de compruba si hay ganador o empate '''

    def cumplio(self,  ficha):

        if self.hay_ganador(self.tablero, ficha):

            return 1

        elif self.hay_empate():

            return 2

    ''' metodo que se encarga de poner en marcha el juego aplicacion los demas metodos definidos '''

    def start(self):

        again = "|Enter| para intentar otra vez"

        Toca = None

        if self.opcion == "b":
            nombres = self.names()
            random.shuffle(nombres)
            name = nombres[0]

        if self.opcion == "c":

            nombres = ["Maquina1 >_<", "Maquina2 ‹_›"]
            name = nombres[0]

        if self.opcion in ("a", "c"):

            Toca = random.choice(["X", "O"])

        name = name if self.opcion in ("b", "c") else ""

        play1, play2 = self.fichas(name)

        ficha = play2 if Toca == play2 else play1

        while True:

            os.system("cls")
            print(self.LOGO)
            tablero(self.tablero)

            # if self.opcion in ("a", "b") :

            if self.opcion != "c" and (ficha == play1 or name != ""):

                while True:
                    os.system("cls")
                    print(self.LOGO)
                    tablero(self.tablero)
                    print()
                    indices = self.escoge_casilla(name)

                    if indices != None:
                        break

                    input(f"{again:>{14+len(again)}} ")

            elif self.opcion == "c":

                turn = "Es Turno De La "
                if ficha == play1:
                    turn = turn + f"{name!r} "
                    youfich = play1
                    otherfich = play2

                else:

                    turn = turn + f"{nombres[1]!r} "
                    youfich = play2
                    otherfich = play1

                print(f"\n{turn:^59}")
                pc = "La Maquina Esta Pensando ..."
                print(f"\n{pc:^59}")

                indices = self.mueve_pc(youfich, otherfich)
                sleep(1.5)

            else:

                turn = "Es Turno De La Maquina"

                print(f"\n{turn:^59}")
                pc = "La Maquina esta pensando …."
                print(f"\n{pc:^59}")

                indices = self.mueve_pc(play2, play1)

                sleep(1.5)

            self.rellenar_tablero(indices[0], indices[1], ficha)

            cumple = self.cumplio(ficha)

            if not (cumple is None):

                if cumple == 2:

                    text = "Han Empatado"
                elif cumple == 1 and ficha == play2 and self.opcion == "a":

                    text = "Te Ha Vencido La PC …"

                elif self.opcion == "c":
                    text = f"Ha Ganado La {name!r}"

                else:

                    text = f'Has Ganado {name!r} ...'

                os.system("cls")
                print(self.LOGO)
                tablero(self.tablero)
                print(f"\n{text:^59}")

                break

            else:

                ficha = play2 if ficha == play1 else play1

                if name != "" and self.opcion != "c":

                    name = nombres[0] if name == nombres[1] else nombres[1]

                if self.opcion == "c":

                    name = nombres[0] if ficha == play1 else nombres[1]

    ''' metodo que devuelve los nombres de los dos jugadores para la opcion b de dos jugadores '''

    def names(self):

        error = "Escoge un nombre valido |Enter| para intentar de nuevo"

        nombres = []
        for i in range(2):

            entry = f"Nombre Del Jugador {i+1}  →  "
            while True:
                os.system("cls")
                print(self.LOGO)

                nom = input(f"{entry:>{12+len(entry)}}")

                if not (nom.isspace()) and len(nom) > 0 and nom.isalnum():

                    sleep(0.5)
                    break

                print()
                input(f"{error:>{8+len(error)}}")

            nombres.append(nom)

        return nombres

    ''' metodo que devuelve las fichas elegidas por los jugadores 
	if opcion es a 
	 el jugador siempre escoge primero 
	elif opcion es b 
	  la eleccion la escoge el jugador que sale al azar
	elif opcion es c
	  se les asignan aleatoriamente las fichas a la maquina 1 y 2 '''

    def fichas(self, name):

        if self.opcion == "a":

            text = "Que Ficha Eliges "

        elif self.opcion == "b":

            text = f"Te Toco Elegir {name!r}"

        else:
            return self.fichas_maquinas()

        fichas = "--- X / O ---"
        entry = "Cual Es Tu Opcion . →   "
        error = "Elige X o O |Enter| para intentar otra vez  "

        while True:

            os.system("cls")
            print(self.LOGO)
            print(f"{text:>{14+len(text)}}")
            print()

            print(f"{fichas:>{14+len(fichas)}}")

            print()
            Opcion = input(f"{entry:>{14+len(entry)}}").upper()

            if (Opcion in ("X", "O")):

                break

            print()
            input(f"{error:>{8+len(error)}}")

        if Opcion == "X":
            return ["X", "O"]
        return ["O", "X"]

    ''' metodo que devuelve las fichas de las maquinas asignadas aleatoriamente '''

    def fichas_maquinas(self):

        os.system("cls")
        maq1 = random.choice(["X", "O"])
        maq2 = "O" if maq1 == "X" else "X"

        tex = ">>>> La Maquina {} Eligio La Ficha {maq!r}"
        tex1, tex2 = tex.format(1, maq=maq1), tex.format(2, maq=maq2)

        print(self.LOGO)
        print(f"{tex1:>{10+len(tex1)}}")
        print()
        print(f"{tex2:>{10+len(tex2)}}")

        line = "_"*(len(tex1)+2)
        print()
        print(f"{line:>{9+len(line)}}")

        con = "|Enter| para comenzar"
        input(f"\n{con:>{18+len(con)}}  ")

        return [maq1, maq2]


''' ------- Fin De La Clase ----- '''


def otra_ronda():

    t = "Deseas jugar Otra Ronda S-N  → "
    opcion = input(f"\n{t:>{14+len(t)}}").upper()

    if opcion == "S":

        return True

    return False


vueltas = True

while vueltas:

    can = magnitud()
    OPCION = juegan(can)
    a = EnRaya(OPCION)

    a.start()

    vueltas = otra_ronda()
