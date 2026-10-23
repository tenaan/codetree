n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))
u.extend(d)
for i in range(n * 2):
    print(u[(i - t) % (n * 2)], end=' ')
    if i == n - 1:
        print()