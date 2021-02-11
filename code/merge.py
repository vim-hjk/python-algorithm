num = [10, 5, 7, 8, 4, 9, 3, 6, 1, 2]
sorted = [None] * 10


def merge(start, end, mid, num):

    left_idx = start
    right_idx = mid + 1
    index = start

    while left_idx <= mid and right_idx <= end:
        if num[left_idx] <= num[right_idx]:
            sorted[index] = num[left_idx]
            left_idx += 1
        else:
            sorted[index] = num[right_idx]
            right_idx += 1
        index += 1
    if left_idx > mid:
        for i in range(right_idx, end + 1):
            sorted[index] = num[i]
            index += 1
    else:
        for i in range(left_idx, mid + 1):
            sorted[index] = num[i]
            index += 1

    for i in range(start, end + 1):
        num[i] = sorted[i]


def mergesort(start, end, num):
    if start < end:
        mid = (start + end) // 2
        mergesort(start, mid, num)
        mergesort(mid + 1, end, num)
        merge(start, end, mid, num)


mergesort(0, 9, num)
print(num)
print(sorted)