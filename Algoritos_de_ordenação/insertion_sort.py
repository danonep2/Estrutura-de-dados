def insertion_sort(lista):
    for i in range(1, len(lista)):
        for j in range(i - 1, -1, -1):
            if (lista[j] > lista[i]):
                lista[j], lista[i] = lista[i], lista[j]
                i -= 1
                continue
            break