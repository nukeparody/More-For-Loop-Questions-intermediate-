def count_primes(start, end):
    count = 0
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                count += 1

    print()
    print(count)

count_primes(1, 100)