import math

def hypotenuse():
    side1 = int(input("what is the length of side 1?"))
    side2 = int(input("what is the length of side 2?"))
    hyp = math.sqrt(side1**2 + side2**2)
    return print(hyp)

hypotenuse()
