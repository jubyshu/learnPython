# maze = [
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1],
#     [1, 0, 0, 0, 1, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1]
# ]
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

from collections import deque


def choose_path(path):
    end_pos = path[-1]
    final_path = []
    while end_pos[2] != -1:
        final_path.append(end_pos[0:2])
        end_pos = path[end_pos[2]]
    final_path.append(end_pos[0:2])
    final_path.reverse()
    for p in final_path:
        print('(%d,%d)' % p)


def find_path(maze, x0, y0, x1, y1):
    queue = deque()
    queue.append((x0, y0, -1))
    m = len(maze) - 1
    n = len(maze[0]) - 1
    walks = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x, y - 1),
    ]
    path = []

    while queue:
        cur_pos = queue.pop()
        path.append(cur_pos)
        if cur_pos[0] == x1 and cur_pos[1] == y1:
            print('You find the path!')
            choose_path(path)
            break

        for walk in walks:
            next_pos = walk(cur_pos[0], cur_pos[1])
            row, col = next_pos[0], next_pos[1]
            # 边界检查
            if (not 0 <= row <= m) or (not 0 <= col <= n):
                next_pos = cur_pos
                continue
            if maze[row][col] == 0:
                queue.append((row, col, len(path) - 1))
                maze[row][col] = 'x'
    else:
        print('There is no path.')


find_path(maze, 0, 0, 4, 4)
