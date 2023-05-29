'''serie fibonacci recursivamente '''


def fibo(n, memory=[0, 1, 1]):

    if len(memory)-1 >= n:
        return memory[n]

    else:

        a, b = fibo(n-1, memory), fibo(n-2, memory)
        memory.append(a+b)

        return a+b


def can_fibo(n, memory=[]):
    lista = []

    if n <= 0:
        return []

    if len(memory) == 0:
        valor = 0

    elif len(memory) == 1:
        valor = 1

    else:

        valor = memory[-1] + memory[-2]

    lista.append(valor)
    memory.append(valor)

    return lista + can_fibo(n-1, memory)


def factorial(n):

    if n <= 1:
        return 1

    else:
        return n * factorial(n-1)


def cant_fact(n, memory=[], cont=0):
    lista = []
    if n == cont:
        return []

    elif len(memory) == 0 or len(memory) == 1:
        valor = 1

    else:
        print(f'{memory= }')
        valor = cont * memory[-1]

    lista.append(valor)
    memory.append(valor)
    cont += 1
    return lista + cant_fact(n, memory, cont)


