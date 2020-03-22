def combinations(array, n, r, index, data, i):
    if index == r:
        for i in range(r):
            print(data[i], end=" ")
        print()
        return
    if i >= n:
        return
    data[index] = array[i]
    combinations(array, n, r, index + 1, data, i + 1)
    combinations(array, n, r, index, data, i + 1)


def print_combinations(array, n, r):
    data = [0] * n
    combinations(array, n, r, 0, data, 0)


array = [int(i) for i in input().split()]
r = int(input())
print_combinations(array, len(array), r)
