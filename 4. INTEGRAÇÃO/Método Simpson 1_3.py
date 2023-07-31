import math

def evaluate_polynomial(coef, x):
    degree = len(coef) - 1
    result = 0
    for i in range(degree + 1):
        result += coef[i] * math.pow(x, degree - i)
    return result

def simpson13(f, a, b):
    h = (b - a) / 2
    return (h / 3) * (f(a) + 4 * f((a + b) / 2) + f(b))

def simpson13_composta(coef, n, a, b):
    h = (b - a) / n
    l = a
    soma = 0
    for i in range(n):
        u = l + h
        soma += simpson13(lambda x: evaluate_polynomial(coef, x), l, u)
        l = u
    return soma

if __name__ == "__main__":
    D = int(input())
    coef = list(map(int, input().split()))
    A, B, N = map(int, input().split())
    resultado = simpson13_composta(coef, N, A, B)
    print("{:.5f}".format(resultado))
