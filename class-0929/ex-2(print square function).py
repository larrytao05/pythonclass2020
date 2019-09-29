# Create a function to print a n by n square using # sign

# def printSquare(n)

def printSquare(n):

    print("#" * n)
    for i in range(1, n-2):
        print("#" + " " * (n-2) + "#")
    print("#" * n)


printSquare(10)
