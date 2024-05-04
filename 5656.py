from collections import deque
from copy import deepcopy


def to_be_deleted(i, g):
    ret = set()
    q = deque()
    for j in range(h):
        if g[j][i] != 0:
            ret.add((j, i))
            q.append((j, i))
            break
    while q:
        x, y = q.popleft()
        for d in range(1, g[x][y]):
            for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                nx, ny = x + d * dx, y + d * dy
                if (
                    0 <= nx < h
                    and 0 <= ny < w
                    and (nx, ny) not in ret
                    and g[nx][ny] != 0
                ):
                    q.append((nx, ny))
                    ret.add((nx, ny))
    return ret


def fall(g):
    for j in range(w):
        q = deque()
        for i in range(h - 1, -1, -1):
            if g[i][j] != 0:
                q.append((g[i][j]))
                g[i][j] = 0
        idx = h - 1
        while q:
            val = q.popleft()
            g[idx][j] = val
            idx -= 1


def dfs(n, g):
    global ans
    if n == 0:
        cnt = 0
        for i in range(h):
            for j in range(w):
                if g[i][j] != 0:
                    cnt += 1
        ans = min(ans, cnt)
        return
    for i in range(w):
        g_copy = deepcopy(g)
        for x, y in to_be_deleted(i, g):
            g_copy[x][y] = 0
        fall(g_copy)
        dfs(n - 1, g_copy)


t = int(input())
for t_num in range(t):
    n, w, h = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(h)]
    ans = w * h
    dfs(n, g)
    print(f"#{t_num+1} {ans}")
