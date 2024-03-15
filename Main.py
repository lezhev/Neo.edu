def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение списка на две части
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Рекурсивная сортировка каждой половины
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Слияние отсортированных половин
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


print(merge_sort([4, 2, 7, 1, 9, 5, 3, 8, 6]))