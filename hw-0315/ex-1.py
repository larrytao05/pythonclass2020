#    If you are provided two lists, cheese=[3,6,3,7,4,6], crackers=[3,6,7,3,2,6],
#    please call this cheese_crackers function and use the total number of cheese and crackers in this list.
#


def cheese_cracker(cheese, crackers):
    total = 0
    for i in range(len(crackers)):
        total += (crackers[i])

    for i in range(len(cheese)):
        total += (cheese[i])

    return total


cheese = [3, 6, 3, 7, 4, 6]
crackers = [3, 6, 7, 3, 2, 6]
print(cheese_cracker(cheese, crackers));


