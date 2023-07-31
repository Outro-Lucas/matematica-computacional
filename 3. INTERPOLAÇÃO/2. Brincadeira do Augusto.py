def menor_grau_polinomio(comprimento, sequencia):
    diferenca = sequencia.copy()
    grau = 0

    while len(set(diferenca)) != 1:
        proxima_diferenca = []
        for i in range(1, len(diferenca)):
            proxima_diferenca.append(diferenca[i] - diferenca[i-1])
        diferenca = proxima_diferenca
        grau += 1

    return grau



if __name__ == "__main__":
    comprimento = int(input())
    sequencia = list(map(int, input().split()))
    print(menor_grau_polinomio(comprimento, sequencia))