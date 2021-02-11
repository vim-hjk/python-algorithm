num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = len(num)
root = 0

left_idx = 2 * root + 1
def heapify(num, root, number):
    index = root
    right_idx = 2 * root + 2
    if left_idx < number and num[left_idx] > num[index]:
        index = left_idx
    if right_idx < number and num[right_idx] > num[index]:
        index = right_idx
    if index != root:
        num[root], num[index] = num[index], num[root]
        heapify(num, index, number)


for i in range(number // 2 - 1, -1, -1):
    heapify(num, i, number)

for i in range(number - 1, 0, -1):
    num[0], num[i] = num[i], num[0]
    heapify(num, 0, i)

print(num)
