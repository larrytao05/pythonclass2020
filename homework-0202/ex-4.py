# Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.
#


def chop(nums):
    del nums[0]
    del nums[len(nums)-1]


nums2 = [5, 10, 14, 235, 4]
print(chop(nums2))
print(nums2)