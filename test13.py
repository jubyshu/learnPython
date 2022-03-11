walks = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1)
]


def seek_path(maze, x1, y1, x2, y2):
    m = len(maze) - 1
    n = len(maze[0]) - 1
    stack = []  # 存放能走的路
    stack.append((x1, y1))

    while len(stack) > 0:
        cur_pos = stack[-1]
        if cur_pos[0] == x2 and cur_pos[1] == y2:
            for p in stack:
                print(p)
        for w in walks:
            next_pos = w(cur_pos[0], cur_pos[1])
            if next_pos[0] < 0 or next_pos[0] > m or next_pos[1] < 0 or next_pos[1] > n:
                next_pos = cur_pos
                continue
            if maze[next_pos[0]][next_pos[1]] == 0:
                stack.append(next_pos)
                # 标记为已走过
                maze[next_pos[0]][next_pos[1]] = 2
                break
        else:
            maze[next_pos[0]][next_pos[1]] = 2
            stack.pop()
    else:
        return False


while True:
    try:
        m, n = int(input()), int(input())
        maze = [list(map(int, input().split())) for _ in range(m)]
        print(seek_path(maze, 0, 0, m - 1, n - 1))
    except:
        break
