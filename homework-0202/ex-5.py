# Write a function called is_sorted that takes a list as a parameter and
# returns True if the list is sorted in ascending order and False otherwise.
#


def is_sorted(nums):
    nums2 = []
    x = 0
    for i in range(len(nums)):
        nums2.append(nums[i])

    nums2.sort()
    for i in range(len(nums)):
        if nums2[i] == nums[i]:
            x += 0
        else:
            x += 1

    if x == 0:
        return True
    else:
        return False


list1 = [3, 5, 6, 78]
list2 = [1, 5, 2, 1, 7]
print(is_sorted(list2))
print(is_sorted(list1))

strings = ["a", "b", "a"]
print(is_sorted(strings))
print(strings)
