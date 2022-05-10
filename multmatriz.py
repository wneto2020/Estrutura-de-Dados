def mult_matriz(a, b):
    mult = []

    for i in range(len(a)):
        mult.append([])
        for j in range(len(b)):
            mult1 = 0
            for k in range(len(a)):
                mult1 += a[i][k] * b[k][j]
            mult[i].append(mult1)
    print(mult)

mult_matriz([[1, 2], [3, 4]], [[-1, 3], [4, 2]])
