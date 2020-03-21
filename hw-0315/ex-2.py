# Define a compare function: if the cheese number is more than crackers, print:
# we have too many cheeses ! If the cracker number is more than cheese, print:
# we have too many crackers. If the amount of cheeses and crackers are the same, print: perfect!.
#


def get_total(l):
    total = 0
    for i in range(len(l)):
        total += (l[i])

    return total


def compare(cheese, crackers):

    if get_total(cheese) > get_total(crackers):
        print("We have too many cheeses!")
    elif get_total(crackers) > get_total(cheese):
        print("We have too many crackers!")
    else:
        print("Perfect!")


cheese = [3, 6, 3, 7, 4, 6]
crackers = [3, 6, 7, 3, 2, 6, 5]
compare(cheese, crackers)