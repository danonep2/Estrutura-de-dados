def quick_sort(array, start=0, end=None):
    global vezes
    vezes += 1
    if (end is None):
        end = len(array) - 1

    if (start < end):
        pivot = partition(array, start, end)
        quick_sort(array, start, pivot - 1)
        quick_sort(array, pivot + 1, end)


def partition(array, start, end):
    pivot = array[end]
    i = start

    for j in range(start, end):
        if (array[j] <= pivot):
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[end] = array[end], array[i]

    return i