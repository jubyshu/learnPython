# n = int(input())
#
# def bottle(num):
#     a = num // 3  # 可换的饮料
#     b = a + num % 3  # 换完后的空瓶
#     if b < 2:
#         a += 0
#     elif b == 2:
#         a += 1
#     else:
#         a += bottle(b)
#     return int(a)
#
# if n > 0:
#     print(bottle(n))

# def manacher(s):
#     s = '#' + '#'.join(s) + '#'
#
#     rad = [0] * len(s)
#     cir = 0
#     max_right = 0
#     max_len = 0
#
#     for i in range(len(s)):
#         if i < max_right:
#             rad[i] = min(rad[cir * 2 - i], max_right - i)
#         else:
#             rad[i] = 1
#
#         while i - rad[i] >= 0 and i + rad[i] < len(s) and s[i - rad[i]] == s[i + rad[i]]:
#             rad[i] += 1
#         if i + rad[i] - 1 > max_right:
#             max_right = i + rad[i] - 1
#             cir = i
#         max_len = max(max_len, rad[i])
#     return max_len - 1
#
#
# str = 'sskabcdfghgfdcbairiroypgkkdlwoogmmbm'
# print(manacher(str))

