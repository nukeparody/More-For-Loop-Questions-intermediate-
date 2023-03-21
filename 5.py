def dice_sums():
    sums = []
    for i in range(1, 7):
        for j in range(1, 7):
            sums.append(i + j)
    sums = list(set(sums)) # Remove duplicates
    sums.sort() # Sort the list
    return [[i, j] for i in sums for j in range(len(sums)) if i+j == sums[j]]

# Example usage
sums = dice_sums()
for row in sums:
    print(row)