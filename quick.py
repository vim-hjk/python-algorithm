num = [10, 5, 7, 8, 4, 9, 3, 6, 1, 2]


def quicksort(start, end, num):
    if start >= end:
        return
    pivot = start
    left_idx = start + 1
    right_idx = end
    while left_idx <= right_idx:
        while left_idx <= end and num[left_idx] < num[pivot]:
            left_idx += 1
        while right_idx > start and num[right_idx] > num[pivot]:
            right_idx -= 1
        if left_idx > right_idx:
            num[right_idx], num[pivot] = num[pivot], num[right_idx]
        else:
            num[left_idx], num[right_idx] = num[right_idx], num[left_idx]

    quicksort(start, right_idx - 1, num)
    quicksort(right_idx + 1, end, num)


quicksort(0, 9, num)
print(num)
