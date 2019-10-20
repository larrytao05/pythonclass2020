"""
Write a function to check if a given number is greater, equal or less than 0
If the number is greater than 0, function should return 1
If the number is equal to 0, function should return 0
If the number is less than 0, function should return -1
"""
def check_value(x):
    if x >= 0:
        if x > 0:
            return 1
        else:
            return 0
    else:
        return -1


print(check_value(5))