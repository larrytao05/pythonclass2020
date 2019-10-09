# In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n!=1×2×…×n
# Write a function getFactorial(n) to calculate the value n! and return it
# Don't use math module in this exercise.


def getFactorial(n):
    i = 0
    sum = 1
    for i in range(n):
        i += 1
        sum = i * sum
    return sum


print(getFactorial(5))
