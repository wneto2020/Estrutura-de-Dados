def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i
        while j > 0 and chave < lista[j-1]:
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = chave

    print(lista)

insertion_sort([1, 2, 5, 4, 3])
