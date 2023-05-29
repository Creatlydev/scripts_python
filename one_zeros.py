import time


def uno(x, l):

    return [x + e for e in l]


memory = [[], ["0", "1"]]


def dos(n, ):

    if n == 1:
        return ["0", "1"]

    else:

        return uno("0", dos(n-1)) + uno("1", dos(n-1))
        # return suma


i = time.time()


print(dos(3))

f = time.time()-i

print(f)
