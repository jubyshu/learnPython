# 最大回文数
# s = 'abba'
# n = len(s)
# r = []
#
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         if s[i:j] == s[i:j][::-1]:
#             r.append(j-i)
# if r != '':
#     print(max(r))

# 删除字符串中出现次数最少的字符
# s = 'aabcddd'
# l = set(s)
# d = {}
#
# for i in l:
#     d[i] = s.count(i)
#
# m = min(d.values())
# w = ''
#
# for i in s:
#     if d[i] != m:
#         w += i
# print(w)

# s = 'a12345'
# p = 'KLMNO'
# AZ = []
# az = []
# ns = ''
# np = ''
#
# for i in range(65, 91):
#     AZ.append(chr(i))
#
# for i in range(97,123):
#     az.append(chr(i))
#
# # 加密
# for j in s:
#     if j.isalpha():
#         if j in AZ:
#             t1 = AZ.index(j)
#             if t1 == 25:
#                 ns += az[0]
#             else:
#                 ns += az[t1 + 1]
#         elif j in az:
#             t2 = az.index(j)
#             if t2 == 25:
#                 ns += AZ[0]
#             else:
#                 ns += AZ[t2 + 1]
#     elif j.isnumeric():
#         if int(j) == 9:
#             ns += '0'
#         else:
#             ns += str(int(j) + 1)
#
# # 解密
# for i in p:
#     if i.isalpha():
#         if i in AZ:
#             t3 = AZ.index(i)
#             if t3 == 0:
#                 np += az[25]
#             else:
#                 np += az[t3 - 1]
#         elif i in az:
#             t4 = az.index(i)
#             if t4 == 0:
#                 np += AZ[25]
#             else:
#                 np += AZ[t4 - 1]
#     elif i.isnumeric():
#         if int(i) == 0:
#             np += '9'
#         else:
#             np += str(int(i) - 1)
#
# print(ns)
# print(np)

def code(string, mode):
    l1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    l2 = 'BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890'
    res = ''
    if mode == 1: # 加密
        for i in string:
            res += l2[l1.index(i)]
    elif mode == 0: # 解密
        for i in string:
            res += l1[l2.index(i)]
    return res