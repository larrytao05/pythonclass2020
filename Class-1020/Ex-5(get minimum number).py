"""
Given two integers, print the smaller value.
"""
def findSmaller2(x, y):
    if x > y:
        print(y)
    elif y > x:
        print(x)
    else:
        print("Number values are equal.")


findSmaller2(11, 10)

"""
Given three integers, print the smaller value.
"""
def findSmaller3(x, y, z):
    if x > y and z > y:
        print(y)
    elif y > x and z > x:
        print(x)
    elif x > z and y > z:
        print(z)
    elif x == z and x != y:
        if y < x:
            print(y)
        else:
            print(x, "=", z)
    elif x == y and x != z:
        if x > z:
            print(z)
        else:
            print(x, "=", y)
    elif y == z and y != x:
        if y > x:
            print(x)
        else:
            print(y, "=", z)
    else:
        print("All numbers are equal. ")


findSmaller3(6, 7, 6)