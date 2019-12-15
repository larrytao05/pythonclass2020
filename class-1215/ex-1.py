fruit = "banana"
print(fruit[0])
len(fruit)
length = len(fruit)
print(fruit[length - 1])

i = 0
while i < len(fruit):
    print(fruit[i])
    i += 1

prefixes = "ABCD"
suffix = " is the coolest letter."
index = 0
while index < len(prefixes):
    print(prefixes[index] + suffix)
    index += 1

string = "ok boomer"
print(string[:2])
print(string[3:])
print(string[:])

new_string = "j" + string[1:]
print(new_string)


def print_backward(x):
    l = len(x) - 1
    while l >= 0:
        print(x[l])
        l -= 1


print_backward("uoy wercs")


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
        return -1


print(find("boomer", "b"))


def count_letter(word, l):
    index = 0
    count = 0
    for letter in word:
        if letter == l:
            count += 1
    print(count)


count_letter(string, "o")

print(string.upper())


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


in_both(fruit, string)


def alpha_order(word1, word2):
    if word1 < word2:
        print(word1 + ", " + word2)
    elif word1 > word2:
        print(word2 + ", " + word1)
    else:
        print("they're the same!")


alpha_order(string, fruit)
