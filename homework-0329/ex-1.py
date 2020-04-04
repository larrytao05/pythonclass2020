def most_cheeses(dic):
    biggest = []
    final = []
    values = list(dic.values())
    keys = list(dic.keys())
    for i in range(len(values)):
        if len(biggest) == 0:
            biggest.append(i)
        elif values[i] == values[biggest[0]]:
            biggest.append(i)
        elif values[i] > values[biggest[0]]:
            biggest = [i]

    for i in range(len(biggest)):
        final.append(keys[biggest[i]])
    return final


dictionary = {"hi": 7, "bob": 3, "clown": 4, "mcdonald's": 7}
print(most_cheeses(dictionary))
