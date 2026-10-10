def count_items(nums):
    if nums == []:
        return 0
    return 1 + count_items(nums[1:])
grades = [3, 5, 2, 4, 3, 5, 4, 2, 3]

result = count_items(grades)
print("Количество элементов в списке:", result)