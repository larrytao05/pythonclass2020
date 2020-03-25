# Define a dictionary, which has name and number of cheeses they bring
# Write a function return the person who bring the most cheeses.
#


def most_cheeses(dic):
    biggest = 0
    values = list(dic.values())
    keys = list(dic.keys())
    for i in range(len(values)):
        if values[i] > biggest:
            biggest = i

    return keys[biggest]


dictionary = {"hi": 2, "bob": 3, "clown": 4}
print(most_cheeses(dictionary))
