# Write a function called getSum(n)
# For the given integer n calculate the following sum: 1+2+...+n and return it
# If n = 5, the function should return 1 + 2 + 3 + 4 + 5 => 15


def getSum(n):
    i = 0
    num = 0
    for i in range(n-1):
        i = i + 1
        num = num + i
        print(i, " + ")
    print(n, " = ", (num + n))


getSum(25)






