
def binary_search(num):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16]
    lista_completa = lista
    size = int((len(lista)) / 2)
    find = False
    while not find:
        if num == lista[size]:
            print(f"Número encontrado no índice {lista_completa.index(num)}")
            break
        elif num > lista[size]:
            lista = lista[size::]
            print(lista)
        elif num < lista[size]:
            lista = lista[0:size]
            print(lista)
        size = int((len(lista)) / 2)

binary_search(20)
