N = int(input())

def re(n):
    if n < 10:
        return n ** 2

    return re(n // 10) + (n % 10) ** 2

print(re(N))