
def f(names):

    if len(names) <= 2:

        return (" and ".join(names) if len(names) == 2 else names[0]) + " like this"

    elif len(names) == 3:

        return f"{names[0]}, {names[1]} and {names[2]} like this"

    else:

        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


print(f(["caro", "jefer", "olga", "maria", "gabriel", "jorge", "samir", "nicol"]))


def likes(names):
    n = len(names)

    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names, others=n-2)


print(likes(["caro", "jefer", "olga", "maria",
      "gabriel", "jorge", "samir", "nicol"]))
