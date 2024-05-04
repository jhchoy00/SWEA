from collections import deque

d = [
    [],
    [(1, 0), (-1, 0), (0, -1), (0, 1)],
    [(1, 0), (-1, 0)],
    [(0, 1), (0, -1)],
    [(-1, 0), (0, 1)],
    [(1, 0), (0, 1)],
    [(1, 0), (0, -1)],
    [(0, -1), (-1, 0)],
]


def bfs(q):
    while q:
        x, y, time = q.popleft()
        if time >= l:
            return
        for dx, dy in d[tunnel[x][y]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and tunnel[nx][ny] != 0:
                flag = False
                for tx, ty in d[tunnel[nx][ny]]:
                    if x == nx + tx and y == ny + ty:
                        flag = True
                        break
                if flag:
                    q.append((nx, ny, time + 1))
                    v[nx][ny] = 1


t = int(input())

for t_num in range(t):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    v = [[0] * m for _ in range(n)]
    v[r][c] = 1
    q = deque([(r, c, 1)])
    bfs(q)
    ans = sum(map(sum, v))
    print(f"#{t_num+1} {ans}")
