def fibonacci(num):
    if num < 0:
        return "Negative numbers not allowed"
    elif result[num] != -1:
        return result[num]
    else:
        result[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return result[num]


n = int(input())
result = [-1] * (n + 1)
result[0] = 0
result[1] = result[2] = 1
print(fibonacci(n))
