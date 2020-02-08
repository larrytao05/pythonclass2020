# Write a function called middle that takes a list
# and returns a new list that contains all but the first and last elements.
#


def middle(nums):
    return nums[1:len(nums) - 1]


nums2 = [1, 5, 6, 10, 3, 5]
print(middle(nums2))
