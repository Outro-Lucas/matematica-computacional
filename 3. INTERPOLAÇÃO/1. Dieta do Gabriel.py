import math

def L(i, x):
    n = len(x)
    num = lambda a: math.prod([(a - x[j]) for j in range(n) if j != i])
    den = lambda a: math.prod([(x[i] - x[j]) for j in range(n) if j != i])
    return lambda a: num(a) / den(a)

def PolinomioLagrange(x, y):
    if len(x) != len(y):
        raise RuntimeError("Tamanho das listas diferentes")
    else:
        n = len(x)
        return lambda a: sum([y[i] * L(i, x)(a) for i in range(n)])

idades = [25, 45, 65]
pesos = [50, 60, 70, 80]
calorias = [
    [2500, 2350, 1900],
    [2850, 2700, 2250],
    [3200, 3000, 2750],
    [3550, 3350, 2850]
]


if __name__ == "__main__":
    idade, peso = map(int, input().split())
    calorias_idade = []
    
    for i in range(len(idades)):
        valores_peso = [calorias[j][i] for j in range(len(idades))]
        polinomio_peso = PolinomioLagrange(pesos[:-1], valores_peso)
        calorias_idade.append(polinomio_peso(peso))
    
    polinomio_idade = PolinomioLagrange(idades, calorias_idade)
    resultado = polinomio_idade(idade)
    
    print(f"{resultado:.5f}")