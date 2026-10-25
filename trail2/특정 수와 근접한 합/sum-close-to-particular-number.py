N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = S
for i in range(N):
    for j in range(i + 1, N):
        c1, c2 = arr[i], arr[j]
        sum = 0
        for k in range(N):
            if i != k and j != k:
                sum += arr[k]
        ans = min(ans, abs(S - sum))

print(ans)