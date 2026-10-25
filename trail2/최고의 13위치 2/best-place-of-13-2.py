n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

"""
000 고정하고 나머지 경우 다 돌기
001 고정하고 동일
"""

ans = 0
for i in range(n): 
    for j in range(n - 2):
        row = arr[i]
        cnt = row[j] + row[j + 1] + row[j + 2]
        for k in range(n):
            for l in range(n - 2):
                # k랑 i가 다르면 l에 아무거나 와도 ㄱㅊ, 같으면 j 에서 더한 영역이 l이랑 절대 겹치면 안됨
                if k == i and len(set([l, l + 1, l + 2, j, j + 1, j + 2])) != 6:
                    continue
                else:
                    row = arr[k]
                    ans = max(ans, cnt + (row[l] + row[l + 1] + row[l + 2]))

print(ans)