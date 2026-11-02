N = int(input())

def recur_sum(n):
    if n == 2:
        return 2
    if n == 1:
        return 1

    return n + recur_sum(n - 2)

print(recur_sum(N)) 