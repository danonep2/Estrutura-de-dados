def bubble_sort(array):
    width = len(array)

    for i in range(width -2, -1, -1):
        for e in range(0, i-1):
            if array[e +1] < array[e]:
                array[e], array[e+1] = array[e+1], array[e]

    return array