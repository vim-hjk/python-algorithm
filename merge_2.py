def mergesort(num):
    if len(num) > 1:
        mid = len(num) // 2
        left = num[:mid]
        right = num[mid:]

        left_list = mergesort(left)
        right_list = mergesort(right)
        return merge(left_list, right_list)
    else:
        return num


def merge(left_list, right_list):
    left_idx = 0
    right_idx = 0
    num = []

    while left_idx < len(left_list) and right_idx < len(right_list):
        if left_list[left_idx] < right_list[right_idx]:
            num.append(left_list[left_idx])
            left_idx += 1
        else:
            num.append(right_list[right_idx])
            right_idx += 1
    while left_idx < len(left_list):
        num.append(left_list[left_idx])
        left_idx += 1
    while right_idx < len(right_list):
        num.append(right_list[right_idx])
        right_idx += 1
    return num


num = [3, 5, 1, 2, 9, 6, 4, 8, 7]
print(mergesort(num))