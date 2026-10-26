N = int(input())

def recur(n):
    if n == N + 1:
        return
    
    print('*' * n)
    recur(n + 1)

recur(1)