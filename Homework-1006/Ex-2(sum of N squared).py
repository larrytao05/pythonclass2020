# Write a function called getSquareSum(n)
# For the given integer n calculate the following sum and return the sum
# 1^2+2^2+3^2+.... n^2


def getSquareSum(n):
    i = 0
    num = 0
    for i in range(n-1):
        i += 1
        num += i
        print((i ** 2), " + ")
    print((n ** 2), " = ", (num ** 2))

getSquareSum(25)
