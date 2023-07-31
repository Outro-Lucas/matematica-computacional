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

    print("0.{} {}".format(binary.ljust(precision, '0'), -contZero))

representationDecimalNumbers(number, base, precision, min_value, max_value)