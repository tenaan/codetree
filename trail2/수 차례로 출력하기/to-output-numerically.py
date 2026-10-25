N = int(input())

def print_n(n):
    if n == N + 1:
        print()
        return

    print(n, end=' ')
    print_n(n + 1)
    print(n, end=' ')

print_n(1)