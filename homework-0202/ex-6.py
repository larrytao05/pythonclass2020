# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.
#


def is_anagram(string1, string2):
    rep_1 = []
    rep_2 = []
    x = 0
    for i in range(len(string1)):
        rep_1.append(string1[i])

    for i in range(len(string2)):
        rep_2.append(string2[i])

    rep_1.sort()
    rep_2.sort()

    for i in range(len(rep_1)):
        if rep_1[i] == rep_2[i]:
            x += 0
        else:
            x += 1

    if x == 0:
        return True
    else:
        return False


anagram1 = "study"
anagram2 = "dusty"
alright = "alright"
print(is_anagram(anagram1, anagram2))
print(is_anagram(anagram2, alright))