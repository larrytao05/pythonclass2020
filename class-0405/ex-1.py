# create new dictionary, using target as key and averaged list as value
#
#
#


def average_dictionary(dic):
    d = {}
    total = 0
    values = list(dic.values())
    keys = list(dic.keys())
    for i in range(len(keys)):
        if type(values[i]) == list:
            total = sum(values[i]) / len(values[i])
            d[keys[i]] = total

    return d


dictionary = {'D0001': [22.71, 22.98, 22.74], 'D0002': [22.92, 23.04, 23.04], 'D0003': [23.47, 23.58, 23.56], 'D0004': [21.73, 21.71, 22.04], 'D0005': [21.64, 21.09, 21.28]}
print(average_dictionary(dictionary))
