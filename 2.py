def square(n_start, n_size):
    square_array = [[0 for j in range(n_size)] for i in range(n_size)]

    count = n_start
    for i in range(n_size):
        square_array[0][i] = count
        count += 1
    for i in range(1, n_size):
        square_array[i][n_size - 1] = count
        count += 1
    for i in range(n_size - 2, -1, -1):
        square_array[n_size - 1][i] = count
        count += 1
    for i in range(n_size - 2, 0, -1):
        square_array[i][0] = count
        count += 1

    print()
    for i in square_array:
        print(i)

square(5, 5)