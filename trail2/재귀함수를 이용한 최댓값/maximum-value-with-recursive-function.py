n = int(input())
arr = list(map(int, input().split()))


def maxcheck(i, max):
    if i == n:
        return max

    max = arr[i] if arr[i] > max else max
    return maxcheck(i + 1, max)

print(maxcheck(0, 0))