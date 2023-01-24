from tests_codewars import test


def path_finder(maze):
    x, y = 0, 0
    stack = [(0, 0)]

    lst_maze = list(map(list, maze.splitlines()))

    while len(stack):
        if lst_maze[-1][-1] == 'x':
            return True
        x, y = stack.pop()
        if lst_maze[x][y] == '.':
            lst_maze[x][y] = 'x'
            for dx, dy in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
                if 0 <= dx < len(lst_maze) and 0 <= dy < len(lst_maze) and lst_maze[dx][dy] == '.':
                    stack.append((dx, dy))
    return lst_maze[-1][-1] == 'x'

# def path_finder(maze):
#     g = maze.splitlines()
#     end, bag = len(g[0]) -1 + len(g) * 1j - 1j, {0}
#     grid = set()
#     for y, l in enumerate(g):
#         for x, c in enumerate(l):
#             if '.' == c:
#                 grid.add(x+y*1j)
#
#     while bag:
#         if end in bag:
#             return True
#         grid -= bag
#         bag = grid & set.union(*({z + 1j ** k for k in range(4)} for z in bag))
#     return False
# tests


def it_1():
    a = "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...W.",
        "...W."])
    test.assert_equals(path_finder(a), True)

    a = "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...WW",
        "...W."])
    test.assert_equals(path_finder(a), False)

    a = "\n".join([
        "..W",
        ".W.",
        "W.."])
    test.assert_equals(path_finder(a), False)

    a = "\n".join([
        ".WWWW",
        ".W...",
        ".W.W.",
        ".W.W.",
        "...W."])
    test.assert_equals(path_finder(a), True)

    a = "\n".join([
        ".W...",
        "W....",
        ".....",
        ".....",
        "....."])
    test.assert_equals(path_finder(a), False)

    a = "\n".join([
        ".W",
        "W."])
    test.assert_equals(path_finder(a), False)


it_1()
