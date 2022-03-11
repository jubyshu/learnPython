# maze = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0]
# ]

maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]


# DFS
def seek_path(maze, x0, y0, x1, y1):
    m, n = len(maze) - 1, len(maze[0]) - 1
    stack = [(x0, y0)]
    walks = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x, y - 1),
    ]
    while stack:
        cur_pos = stack[-1]
        if cur_pos[0] == x1 and cur_pos[1] == y1:
            print('You find the path!')
            for s in stack:
                print('(%d,%d)' % s)
            break
        for walk in walks:
            next_pos = walk(cur_pos[0], cur_pos[1])
            row, col = next_pos[0], next_pos[1]
            if (not 0 <= row <= m) or (not 0 <= col <= n):
                next_pos = cur_pos
                continue
            if maze[row][col] == 0:
                stack.append(next_pos)
                maze[row][col] = 'x'
                break
        else:
            stack.pop()
    else:
        print('There is no path')


# seek_path(maze, 0, 0, 4, 4)
seek_path(maze, 1, 1, 5, 5)
