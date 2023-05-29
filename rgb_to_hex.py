def rgb(r, g, b):

    def round(x): return min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


print(rgb(230, 20, 7))


def rgb(r, g, b):

    return '%06X' % (
        max(0, min(255, r)) << 16 |
        max(0, min(255, g)) << 8 |
        max(0, min(255, b)))


print(rgb(230, 20, 7))
