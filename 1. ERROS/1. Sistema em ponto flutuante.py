from fractions import Fraction

beta, p, m, M = [ int(x) for x in input().split()]

max_num = Fraction()
mul = Fraction(1, beta)
base = Fraction(beta-1, beta)
for i in range(p):
	max_num += base
	base *= mul

max_num *= Fraction( beta**M, 1)

mult = Fraction(1, beta)
base = Fraction(1, beta)
for i in range(-m):
	base *= mul

print(str(max_num.numerator) + "/" + str(max_num.denominator))
print(str(base.numerator) + "/" + str(base.denominator))