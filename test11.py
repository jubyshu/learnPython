# 动态规划
# 编辑距离
# def edit_distance(s1, s2):
#     m, n = len(s1), len(s2)
#
#     dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # (m+1) * (n+1)
#
#     for i in range(m + 1):
#         dp[i][0] = i
#     for j in range(n + 1):
#         dp[0][j] = j
#
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
#     return dp[m][n]

# 合唱队
def len_of_seq(nums):
    # 以第i个人为中心左侧的合唱队长度
    n = len(nums)
    les = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                les[i] = max(les[i], les[j] + 1)
    return les


nums = [186, 186, 150, 200, 160, 130, 197, 200]
n = len(nums)
m1, m2 = len_of_seq(nums), len_of_seq(nums[::-1])[::-1]
res = [m1[i] + m2[i] - 1 for i in range(len(nums))]

print(n - max(res))