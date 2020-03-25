# write a function to generate a NEW LIST, in which every element is a[i]+1 (list A should not be touched,
# please print both A and B to confirm it).
#


def add_one(a):
    b = []
    for i in range(len(a)):
        b.append(a[i] + 1)

    print(a, b)


nums = [1, 3, 5, 6]
add_one(nums)


