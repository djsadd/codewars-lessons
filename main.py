def path_finder(maze):
    lst = maze.split()
    stack = []

    x, y = 0, 0
    move_x, move_y = 1, 0
    for row in lst:
        print(row)
    while True:
        if len(lst)-1 == x and lst[x][y+move_y] != 'W':
            move_x, move_y = move_y, move_x
        if lst[x+move_x][y+move_y] != 'W':
            x += move_x
            y += move_y
        if x == len(lst)-2 and y == len(lst)-2:
            break

    return True


a = "\n".join([
    ".W.",
    ".W.",
    "..."
])
print(path_finder(a))  # 4

b = "\n".join([
    ".W.",
    ".W.",
    "W.."
])
print(path_finder(b))  # False

c = "\n".join([
    "......",
    "......",
    "......",
    "......",
    "......",
    "......"
])
print(path_finder(c))  # 10


d = "\n".join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "....W."
])

print(path_finder(d))  # False

a = "\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...W.",
          "...W."])

print(path_finder(a))