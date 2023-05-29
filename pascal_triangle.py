def func(n):

    if n > 0:

        # print("*"*n)
        func(n-1)
        print("*"*(n), "-")
        func(n-1)


# funcion que devuelve la suma de los numeros de a a dos de la lista pasada y añade siempre dos unos uno al final de la lista y otro al inicio   ejemplo : [1, 1] devuelve ->							 [1, 2, 1]
def sumar(l):

    sumas = []

    for i in range(len(l)-1):

        suma = l[i] + l[i+1]
        sumas.append(suma)

    return [1] + sumas + [1]


def pascal(n):

    triangPascal = []
    original = []

    tab = n*3-1

    for x in range(n):

        # original.append([])

        if x == 0:

            original.append([])
            triangPascal.append(f"{1:>{tab+1}}")

            original[x].append(1)
            tab -= 5

        else:

            sumas = sumar(original[x-1])
            fila = " "*(tab)
            for nm, i in enumerate(sumas):

                fila += f"{i:_^5}{'|' if nm != len(sumas)-1 else ''}"

            original.append(sumas)
            triangPascal.append(fila)

            tab -= 3

    return "\n".join(triangPascal)


print(pascal(10))


'''
              1
         __1__ __1__
      __1__ __2__ __1__
   __1__ __3__ __3__ __1__
__1__ __4__ __6__ __4__ __1__    
  
_1_ _5_ 10_ 10_ _5_ _1_

'''
