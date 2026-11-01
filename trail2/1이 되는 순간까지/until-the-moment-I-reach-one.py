N = int(input())

def recur(n, cnt):
    if n == 1:
        return cnt

    if n % 2 == 0:
        return recur(n // 2, cnt + 1)
    elif n % 2 == 1:
        return recur(n // 3, cnt + 1)


print(recur(N, 0))