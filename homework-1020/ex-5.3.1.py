def is_triangle(x, y, z):
    if x + y >= z and x + z >= y and y + z >= x:
        print("Yes")
    else:
        print("No")


is_triangle(5, 11, 5)
