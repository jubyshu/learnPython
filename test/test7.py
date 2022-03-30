# 找出最长的递增的子序列的长度
nums = [1, 5, 2, 4, 3]

memo = {}


# def L(nums, i):
#     if i in memo:
#         return memo[i]
#
#     if i == len(nums) - 1:
#         return 1
#
#     max_len = 1
#     for j in range(i + 1, len(nums)):
#         if nums[j] > nums[i]:
#             max_len = max(max_len, L(nums, j) + 1)
#
#     memo[i] = max_len
#     return max_len


# def length_of_LIS(nums):
#     return max(L(nums, i) for i in range(len(nums)))

def length_of_LIS(nums):
    n = len(nums)
    L = [1] * n

    for i in reversed(range(n)):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                L[i] = max(L[i], L[j] + 1)

    return max(L)


print(length_of_LIS(nums))
