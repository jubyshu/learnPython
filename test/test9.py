# DFS

# res = []
#
#
# def dfs(wait, stack, out):
#     if not wait and not stack:
#         res.append(' '.join(map(str, out)))
#     if wait:
#         dfs(wait[1:], stack + [wait[0]], out)
#     if stack:
#         dfs(wait, stack[:-1], out + [stack[-1]])
#
#
# dfs([1, 2, 3], [], [])
# print(res)

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# res = set()
# for i in range(0, len(height) - 1):
#     for j in range(i + 1, len(height)):
#         res.add((j - i) * min(height[i], height[j]))
# print(max(res))

# n, m = map(int, input().split())
# dp = [[1 for i in range(n + 1)] for j in range(m + 1)]
#
# for i in range(1, m + 1):
#     for j in range(1, n + 1):
#         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# print(dp[m][n])

# def func(x, y):
#     if x == 0 or y == 0:
#         return 1
#     else:
#         return func(x - 1, y) + func(x, y - 1)
#
#
# a, b = map(int, input().split())
# c = func(a, b)
# print(c)



