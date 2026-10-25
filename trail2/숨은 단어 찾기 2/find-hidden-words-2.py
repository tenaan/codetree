n, m = map(int, input().split())
arr = [input() for _ in range(n)]

# 상하좌우 상좌 상우 하좌 하우
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

# 범위 체크 함수
def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

# LEE 찾기
def find_lee(x, y):
    count = 0
    if arr[x][y] != 'L':
        return False

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        nx2 = nx + dx[d]
        ny2 = ny + dy[d]
        if in_range(nx, ny) and in_range(nx2, ny2) and arr[nx][ny] == 'E' and arr[nx2][ny2] == 'E':
            count += 1
         
    return count

cnt = 0
for i in range(n):
    for j in range(m):
        cnt += find_lee(i, j)

print(cnt)