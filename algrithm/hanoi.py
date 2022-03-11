# 汉诺塔问题
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('moving from {0} to {1}'.format(a, c))
        hanoi(n - 1, b, a, c)


hanoi(3, 'A', 'B', 'C')
