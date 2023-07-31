import math


def L(i, x):
    n = len(x)
    num = lambda a: math.prod([(a - x[j]) for j in range(n) if j != i])
    den = math.prod([(x[i] - x[j]) for j in range(n) if j != i])
    return lambda a: num(a) / den


def PolinomioLagrange(x, y):
    if len(x) != len(y):
        raise RuntimeError("tamanho das listas diferentes")
    else:
        n = len(x)
        return lambda a: sum([y[i] * L(i, x)(a) for i in range(n)])


def mopSum(D, coeficientes):
    x = []
    y = []
    mop = 1

    for n in range(1, D + 1):
        sum = 0
        i = 1
        while i <= len(coeficientes):
            sum += (coeficientes[i - 1]) * n ** (D - (i - 1))
            i += 1

        x.append(n)
        y.append(sum)
        p = PolinomioLagrange(x, y)

        if len(x) > 1:
            for j in range(len(x) - 1, len(x)):
                aux = 0
                stop = False
                while not stop:
                    px = x[j]
                    py = y[j]
                    if p(px) == py:
                        k = px
                        while k <= px + 1:
                            aux = p(k)
                            k += 1
                        mop += aux
                        stop = True
    return mop


if __name__ == "__main__":
    D = int(input())
    coeficientes = list(map(int, input().split()))
    print(int(mopSum(D, coeficientes)))
