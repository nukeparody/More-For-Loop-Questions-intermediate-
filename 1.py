def multiplication(n_rows, n_cols):
    table = [[0 for j in range(n_cols)] for i in range(n_rows)]

    for i in range(n_rows):
        for j in range(n_cols):
            table[i][j] = (i + 1) * (j + 1)

    for row in table:
        print(row)

multiplication(12, 12)
