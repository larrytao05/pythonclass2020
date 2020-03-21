def has_duplicates(list):
    d = dict()
    l = len(list)
    for i in range(l):
        if list[i] in dict():
            dict[list[i]] == 1
        else:
            dict[list[i]] += 1
    for c in dict:
        if dict(c) > 1:
            return True
        else:
            return False


l = [1, 3, 5, 6, 6]
has_duplicates(l)