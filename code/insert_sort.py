num = [10, 5, 7, 8, 4, 9, 3, 6, 1, 2]
for i in range(0, 9):
    j = i
    while j >= 0 and num[j] > num[j + 1]:
        num[j], num[j + 1] = num[j + 1], num[j]
        j -= 1
print(num)