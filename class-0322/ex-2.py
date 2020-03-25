

def max(ls):
    biggest = 0
    for i in range(len(ls)):
        if i > 0:
            if ls[i] > biggest:
                biggest = ls[i]

        if i == 0:
            biggest = ls[0]

    return biggest


l = [8, 3, 5, 6]
print(max(l))