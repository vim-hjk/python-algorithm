num = [10, 5, 7, 8, 4, 9, 3, 6, 1, 2]
for i in range(0, 9):
    min = 9999
    for j in range(i, 10):
        if num[j] < min:
            index = j
            min = num[j]
    num[i], num[index] = num[index], num[i]
print(num)