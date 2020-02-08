# Write a function called has_duplicates that takes a list
# and returns True if there is any element that appears more than once. It should not modify the original list.
#


def has_duplicates(list1):
    rep_1 = []
    i = 1
    for i in range(len(list1)):
        rep_1.append(list1[i])

    rep_1.sort()
    for i in range(len(rep_1)):
        if rep_1[i] == rep_1[i-1]:
            return True

    return False


nums = [1, 3, 5, 2]
nums1 = [1, 3, 2, 2]
strings = ['a', 'c', 'b', 'b']
print(has_duplicates(nums))
print(has_duplicates(nums1))
print(has_duplicates(strings))


