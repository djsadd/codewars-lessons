def path_finder(maze):
    lst_maze = maze.split()
    x, y = 0, 0
    end_x, end_y = len(lst_maze)-1, len(lst_maze)-1

    for row in lst_maze:
        print(row)

    return True


a = "\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...W.",
          "...W."])
print(path_finder(a))