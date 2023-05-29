

def tablero_per(t):

    p = " "
    long = len(t)
    casilla = 0
    tab = 0
    fill= 0
    if long == 3:
        espa = 15
        spac = 8
        fill = 5

    elif long == 4:
        espa = 10
        spac = 7
        fill = 4

    elif long == 5:
        espa = 8
        spac = 6
        fill = 4

    for x in range(long):

        for j in range(fill):
            print(f"{p:>{espa}}", end="")
            for i in range(long):
                # casilla += 1
                content = t[x][i]
                if content == 'X':
                    if spac % 2 != 0:
                        espacios = (spac+2) // 2
                    else:
                        espacios = (spac+2) // 2 - 1
                    content = f'{" " * espacios}' + \
                        '\033[1;37;42m' + content + \
                        '\033[0;m' + f'{" " * ((spac+2)//2)}'

                elif content == 'O':
                    if spac % 2 != 0:
                        espacios = (spac+2) // 2
                    else:
                        espacios = (spac+2) // 2 - 1
                    content = f'{" " * espacios}' + \
                        '\033[1;37;44m' + content + \
                        '\033[0;m' + f'{" " * ((spac+2)//2)}'

                if j == 0:
                    casilla += 1
                    print(f"  {casilla:<{spac}}",
                          end="|" if i != (long-1) else "")

                elif j == 2:
                    print(f"{content:^{spac+2}}",
                          end="|" if i != (long-1) else "")
                    tab += 1

                else:
                    print(f"  {p:<{spac}}", end="|" if i != (long-1) else "")
            print()

        if x != long-1:

            g = "-"*(spac+2)
            print(f"{p:>{espa}}", end="")
            for k in range(long):

                print(f"{g}", end="±" if k != long-1 else "")

            print()


def tablero_matriz(t):
    """_summary_

    Args:
        t (_type_): _description_
    """

    p = " "
    long = len(t)
    casilla = 0
    tab = 0
    fila = 0

    if long == 3:
        espa = 14
        spac = 8
        fill = 4

    elif long == 4:
        espa = 10
        spac = 7
        fill = 4

    elif long == 5:
        espa = 8
        spac = 6
        fill = 4

    def line():
        g = "-"*(spac+2)
        print(f"{p:>{espa}}", end="±")
        for k in range(long):

            print(f"{g}", end="±")

        print()
    print(f"{p:{espa}}", end=" ")
    for i in range(long):
        casilla += 1
        print(f"{casilla:^{spac+2}}", end=" ")

    print()
    line()
    casilla = 0

    for x in range(long):
        casilla += 1

        for j in range(fill):
            print(f"{p:>{espa}}" if j !=
                  2 else f"{casilla:{espa-1}} ", end="|")
            row = 0
            for i in range(long):

                if j == 2:

                    print(f"{t[fila][row]:^{spac+2}}", end="|")
                    row += 1

                else:
                    print(f"  {p:<{spac}}", end="|")
            print()

        fila += 1

        line()



# def tablero_per(t):
#     long = len(t)
#     p = " "
#     tab = 0
#     if long == 3:
#         espa = 15
#         spac = 8
#         fill = 5
#     elif long == 4:
#         espa = 10
#         spac = 7
#         fill = 4
#     elif long == 5:
#         espa = 8
#         spac = 6
#         fill = 4

#     def imprimir_separador():
#         g = "-" * (spac + 2)
#         print(f"{p:>{espa}}±{g}" * long)

#     def imprimir_numero_casilla(casilla):
#         print(f"  {casilla:<{spac}}", end="|")

#     def imprimir_contenido_celda(content):
#         if spac % 2 != 0:
#             espacios = (spac + 2) // 2
#         else:
#             espacios = (spac + 2) // 2 - 1

#         if content == 'X':
#             content = f'{" " * espacios}\033[1;37;42m{content}\033[0;m{" " * ((spac + 2) // 2)}'
#         elif content == 'O':
#             content = f'{" " * espacios}\033[1;37;44m{content}\033[0;m{" " * ((spac + 2) // 2)}'

#         print(f"{content:^{spac + 2}}", end="|")

#     for x in range(long):
#         imprimir_separador()

#         for j in range(fill):
#             imprimir_numero_casilla((x * fill) + j + 1)

#             for i in range(long):
#                 content = t[x][i]
#                 imprimir_contenido_celda(content)

#             print()
#             if j == 2:
#                 tab += 1

#     imprimir_separador()


# def tablero_matriz(t):
#     long = len(t)
#     p = " "

#     if long == 3:
#         espa = 14
#         spac = 8
#         fill = 4
#     elif long == 4:
#         espa = 10
#         spac = 7
#         fill = 4
#     elif long == 5:
#         espa = 8
#         spac = 6
#         fill = 4

#     def imprimir_separador():
#         g = "-" * (spac + 2)
#         print(f"{p:>{espa}}±{g}" * long)

#     def imprimir_numero_casilla(casilla):
#         print(f"{p:>{espa}}|{casilla:{espa - 1}}", end="|")

#     def imprimir_contenido_celda(content):
#         print(f"{content:^{spac + 2}}", end="|")

#     imprimir_numero_casilla(" ")
#     for i in range(long):
#         imprimir_numero_casilla(i + 1)
#     print()
#     imprimir_separador()

#     for x in range(long):
#         for j in range(fill):
#             imprimir_numero_casilla(x + 1)
#             for i in range(long):
#                 content = t[x][i]
#                 imprimir_contenido_celda(content)
#             print()
#             if j == 2:
#                 tab += 1
#         imprimir_separador()



# l = [
#     [0, 0, 0]
# ] * 3

# tablero_per(l)