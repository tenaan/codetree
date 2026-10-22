board = [list(map(int, input().split())) for _ in range(19)]

# 바둑알의 위치를 찾고 위, 아래 대각선으로 양옆으로 2개의 바둑알이 존재하는지 탐색

def search_vertical(n, x, y):
    # 2개 위 2개 아래 : 세로줄
    dx = [-2, -1, 1, 2]
    for d in dx:
        nx = x + d
        if check_range(nx, y):
            if board[nx][y] != n:
                return False
    return True

def search_horizon(n, x, y):
    # 2개 가로줄
    dy = [-2, -1, 1, 2]
    for d in dy:
        ny = y + d
        if check_range(x, ny):
            if board[x][ny] != n:
                return False
    return True

def search_leftcross(n, x, y):
    ds = [-2, -1, 1, 2]
    for d in ds:
        nx = x + d
        ny = y + d
        if check_range(nx, ny):
            if board[nx][ny] != n:
                return False
    return True

def search_rightcross(n, x, y):
    ds = [(-2, 2), (-1, 1), (1, -1), (2, -2)]
    for dx, dy in ds:
        nx = x + dx
        ny = y + dy
        if check_range(nx, ny):
            if board[nx][ny] != n:
                return False
    return True


def search(n, x, y):
    if search_vertical(n, x, y) or search_horizon(n, x, y) or search_leftcross(n, x, y) or search_rightcross(n, x, y):
        return True

def check_range(x, y):
    if 0 <= x < 19 and 0 <= y < 19:
        return True
    return False

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            if search(board[i][j], i, j) :
                print(board[i][j])
                print(i + 1, j + 1)
                exit()

print(0)
