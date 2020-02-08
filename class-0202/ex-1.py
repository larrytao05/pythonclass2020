# Write a function called nested_sum that takes a list of lists of integers
# and adds up the elements from all of the nested lists.


def nested_sum(x):
    sum_final = 0
    for i in range(len(x)):
        sum_final += sum(x[i])

    return sum_final


nums = [[5, 4], [6, 7]]
print(nested_sum(nums))
