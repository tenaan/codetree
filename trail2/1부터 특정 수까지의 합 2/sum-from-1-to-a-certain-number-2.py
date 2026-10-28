N = int(input())

def r_sum(n):
    if n == 1:
        return 1

    return r_sum(n - 1) + n

print(r_sum(N))