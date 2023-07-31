from fractions import Fraction

number = float(input())
base, precision, min_value, max_value = input().split()
base = int(base)
precision = int(precision)
min_value = int(min_value)
max_value = int(max_value)

def representationDecimalNumbers(number: float, base: int, precision: int, min_value: int, max_value: int):
    value = number
    binary = ""
    partInt = 0
    contZero = 0
    partFrac = 0.0
    top_value = False

    while len(binary) < precision:
        _value = value * base
        partInt = int(_value)
        partFrac = _value - partInt
        
        if partInt == 1:
            top_value = True        
        if top_value:
            binary += str(partInt)
        else:
            contZero += 1
        
        value = partFrac

    mantissa = int(binary, base=2) / base**precision
    exponent = -contZero
    
    if exponent < min_value:
        print("underflow")
    else:
        print(Fraction(mantissa * base**exponent).limit_denominator())
        abs_error = abs(number - float(mantissa * base**exponent))
        ulp = base**(exponent - precision + 1)
        result = Fraction(abs_error * 10 * ulp).limit_denominator()
        print(Fraction(result.numerator, 1280).limit_denominator())

representationDecimalNumbers(number, base, precision, min_value, max_value)