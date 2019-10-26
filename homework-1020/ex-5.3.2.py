def is_triangle(x, y, z):
    if x + y >= z and x + z >= y and y + z >= x:
        print("Yes")
    else:
        print("No")


def triangle_cool():
    x = int(input("Input the length of the triangle's first side: "))
    y = int(input("Input the length of the next side: "))
    z = int(input("input the length of the last side: "))

    is_triangle(x, y, z)


triangle_cool()