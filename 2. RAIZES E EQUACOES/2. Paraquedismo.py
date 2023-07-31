def bissecao(coef_arrasto, velocidade_maxima, tempo):
    epsilon = 0.001
    a = 50.0
    b = 100.0
    
    while (b - a) > epsilon:
        m = (a + b) / 2
        v = (m * 9.8 / coef_arrasto) * (1 - pow(2.71828, -coef_arrasto * tempo / m)) - velocidade_maxima
        if v == 0:
            break
        if v * ((a * 9.8 / coef_arrasto) * (1 - pow(2.71828, -coef_arrasto * tempo / a)) - velocidade_maxima) < 0:
            b = m
        else:
            a = m
    return round(m, 2)

if __name__ == "__main__":
    coef_arrasto, velocidade_maxima, tempo = [float(x) for x in input().split()]
    massa_minima = bissecao(coef_arrasto, velocidade_maxima, tempo)
    print("{:.2f}".format(massa_minima))