def CountRoutes(n):
    result = 2 

    for i in range(1, n):
        result = int(result * (n + i)/i)
    return result

print(CountRoutes(20))