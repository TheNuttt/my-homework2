grades = [4, 2, 5, 3, 5, 4, 3]
n = len(grades)

# arr_asc = grades.copy()
# for i in range(n - 1):
#     min_i = i

#     for j in range(i + 1, n): 
#         if arr_asc[j] < arr_asc[min_i]:
#             min_i = j

#     temp = arr_asc[i]
#     arr_asc[i] = arr_asc[min_i]     
#     arr_asc[min_i] = temp
# print("По возрастанию:", arr_asc)      
arr_desc = grades.copy()

for i in range(n - 1):
    max_i = i

    for j in range(i + 1, n):
        if arr_desc[j] > arr_desc[max_i]:
            max_i = j

    temp = arr_desc[i]            
    arr_desc[i] = arr_desc[max_i]
    arr_desc[max_i] = temp
print("По убыванию:", arr_desc)#