def ordenar(s):

    # s = s.split()

    n = sorted(s.split(), key=lambda x: list(filter(str.isdigit, x)))

    return " ".join(n)


print(ordenar("hab3 bd4 5er h0"))


def order(sentence):

    return " ".join(sorted(sentence.split(), key=lambda x: list(filter(str.isdigit, x))))


print(order("h2 O8 es4te n00rt el3s"))


def order(words):

    a = (sorted(words.split(), key=lambda w: sorted(w)))

    return a


print(order("h2 a8a es4te n00rt el3s"))
