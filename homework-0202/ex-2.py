# Write a function called cum_sum that takes a list of numbers and returns the cumulative sum;
# that is, a new list where the ith element is the sum of the first i+1 elements from the original list.
#


def cum_sum(nums):
    nums2 = []
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        nums2.append(sum)

    return nums2


lil_huddy = [1, 2, 3]
print(cum_sum(lil_huddy))
lil_huddy[2] = 5;
print(cum_sum(lil_huddy))
