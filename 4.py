def count_zeros(start, end):
    count = 0
    for num in range(start, end + 1):
        if '0' in str(num):
            count += 1

    print()
    print(count)

count_zeros(1, 100)