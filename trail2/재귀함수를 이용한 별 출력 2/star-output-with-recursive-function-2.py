n = int(input())

def recur(N):
    if N == 0:
        return

    print('* ' * N)
    recur(N - 1)
    print('* ' * N)

recur(n)