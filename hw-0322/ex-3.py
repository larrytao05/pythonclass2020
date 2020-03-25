# find kth largest element in an array.


def search_by_size(arr, k):
    temp_list = list(arr)
    temp_list.sort(reverse=True)
    return temp_list[k - 1]


nums = [5, 2, 7, 1, 46]
print(search_by_size(nums, 5))


