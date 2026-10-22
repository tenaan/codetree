from collections import deque

dq = deque()

n = int(input())

for _ in range(n):
    cmds = input().split()
    cmd = cmds[0]
    if cmd == 'push_back':
        dq.append(cmds[1])
    elif cmd == 'push_front':
        dq.appendleft(cmds[1])
    elif cmd == 'pop_front':
        print(dq.popleft())
    elif cmd == 'pop_back':
        print(dq.pop())
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        print(int(0 if dq else 1))
    elif cmd == 'front':
        print(dq[0])
    elif cmd == 'back':
        print(dq[-1])