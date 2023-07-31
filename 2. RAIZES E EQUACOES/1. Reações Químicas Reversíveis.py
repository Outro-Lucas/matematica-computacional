def truncate(f, n):
    """Truncates/pads a float f to n decimal places without rounding"""
    s = "%.12f" % f
    i, p, d = s.partition(".")
    return ".".join([i, (d + "0" * n)[:n]])


def calculateMols(X, Ca, Cb, Cc):
    return (Cc + X) / (((Ca - 2 * X) ** 2) * (Cb - X))

def findValue(K, Ca, Cb, Cc, Xl, Xu, N):
    while abs(Xu - Xl) > 0.5 * 10 ** (-N):
        Xm = (Xl + Xu) / 2
        K_Xm = calculateMols(Xm, Ca, Cb, Cc)
        if K_Xm < K:
            Xl = Xm
        else:
            Xu = Xm
    return Xm


if __name__ == "__main__":
    K, Ca, Cb, Cc, Xl, Xu, N = [float(x) for x in input().split()]
    X = findValue(K, Ca, Cb, Cc, Xl, Xu, int(N))
    print(truncate(X, int(N)))