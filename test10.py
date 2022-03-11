# Snake Matrix
# n = int(input())
# dp = [[0] * n for i in range(n)]
# # print(dp)
# for i in range(n):  # 行
#     for j in range(n - i): # 列
#         if j == 0:
#             if i == 0:
#                 dp[i][j] = 1
#             else:
#                 dp[i][j] = dp[i - 1][j] + i
#         else:
#             dp[i][j] = dp[i][j - 1] + (i + j + 1)
#         print(dp[i][j], end=' ')
#     print('\r')

# def plate(m, n):
#     if m < 0 or n < 0:
#         return 0
#     elif m == 1 or n == 1:
#         return 1
#     else:
#         return plate(m, n - 1) + plate(m - n, n)
#
#
# print(plate(20, 5))

# def is_power(n):
#     if n == 1:
#         return True
#     elif n % 2 != 0:
#         return False
#     else:
#         return is_power(n // 2)
#
# print(is_power(28))
