def bubble_sort(lista):
    n = 1
    for i in range(len(lista)-n):
        for j in range(len(lista)-n):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

        n += 1
    print(lista)


bubble_sort([5, 4, 3, 2, 1])