# Create a dictionary start with 3 lists:

name=['Scarlett','Larry','Jason','Ava','Lucas']
Crackers=[3,5,1,2,9]
Cheeses=[2,7,13,5,3]


def two_value_dictionary(k, v1, v2):
    dic = {}
    vals = []
    for i in range (len(k)):
        vals.append((v1[i], v2[i]))
        dic[k[i]] = {vals[i]}

    return dic


print(two_value_dictionary(name, Crackers, Cheeses))
