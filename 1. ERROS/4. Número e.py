epsilon = float(input())

approx_e = 1
previous_approx_e = 0

i = 1

while True:
    term = 1
    for j in range(1, i + 1):
        term *= j
    approx_e += 1 / term
    
    if abs(approx_e - previous_approx_e) / approx_e < epsilon:
        break
    
    previous_approx_e = approx_e
    i += 1

print("{:.15f}".format(approx_e))