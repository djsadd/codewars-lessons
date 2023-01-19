from collections import deque
from tests_codewars import test


def path_finder(maze):
    maze = list(map(list, maze.splitlines()))
    t = (len(maze)-1, len(maze)-1)
    s = (0, 0)
    n = len(maze)
    m = len(maze[0])
    d = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append(s)

    while len(queue) != 0:
        x, y = queue.popleft()
        if maze[x][y] == 'x':
            continue

        maze[x][y] = 'x'
        if maze[-1][-1] == 'x':
            return d[t[0]][t[1]]

        for dx, dy in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if 0 <= dx < n and 0 <= dy < m and maze[dx][dy] != 'W':
                d[dx][dy] = d[x][y]+1
                queue.append([dx, dy])
    return d[t[0]][t[1]]


a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

test.assert_equals(path_finder(a), 4)
test.assert_equals(path_finder(b), False)
test.assert_equals(path_finder(c), 10)
test.assert_equals(path_finder(d), False)
