def factorial_assignment(n):
    result = [-1] * (n + 1)
    result[0] = result[1] = 1
    return factorial(n, result)


def factorial(num, result):
    if result[num] != -1:
        return result[num]
    else:
        result[num] = num * factorial(num-1, result)
        return result[num]


n = int(input())
print(factorial_assignment(n))
