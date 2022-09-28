arr =[1, 424, -4, 0, 32]
min_n = arr [0]
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:

                nums[i], nums[i + 1] = nums[i + 1], nums[i]

                swapped = True

bubble_sort(arr)
print(arr)

for i in arr:
    if (i < min_n):
        min_n = i

print(min_n)

max_n = arr [0]

for i in arr:
    if (i > max_n):
        max_n = i
print (max_n)



