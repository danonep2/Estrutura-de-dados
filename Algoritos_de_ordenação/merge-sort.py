def merge_sort(array):
    if (len(array) <= 1):
        return

    mid = len(array) // 2
    array_left = array[:mid]
    array_right = array[mid:]
    merge_sort(array_left)
    merge_sort(array_right)

    li = ri = k = 0

    while (li < len(array_left) and ri < len(array_right)):
        if (array_left[li] <= array_right[ri]):
            array[k] = array_left[li]
            li += 1
        else:
            array[k] = array_right[ri]
            ri += 1
        k += 1

    while (li < len(array_left)):
        array[k] = array_left[li]
        li += 1
        k += 1

    while (ri < len(array_right)):
        array[k] = array_right[ri]
        ri += 1
        k += 1
