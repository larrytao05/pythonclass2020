# As an exercise, modify find so that it has a third parameter, the index in word where it should start looking.
#
# first version of find:
#   def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index += 1
#         return -1
#


def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


print(find("hi", "i", 1))


def letter_in_word(letter, word):
    return letter in word


print(letter_in_word("a", "banana"))

word = "hi"
index = word.find("i")
print(index)
