# while True:
#     try:
#         f = input()
#         xs = '0.' + f.split(sep='.')[-1]
#         if float(xs) > 0.5:
#             print(round(float(f)))
#         elif float(xs) == 0.5:
#             print(int(float(f)) + 1)
#         else:
#             print(int(float(f)))
#     except:
#         break

# n = float(input())
# print(int(n + 0.5))

# 质因数
# n = int(input())
# for i in range(2, int(n ** 0.5) + 1):
#     while n % i == 0:
#         print(i, end = ' ')
#         n = n // i
# if n > 2:
#     print(n)

# s = '9876673'
# l = ''
# for i in s[::-1]:
#     if i not in l:
#         l += i
# print(int(l))

# s = input()
# ns =''
# for l in s:
#     if l.isalpha():
#         ns += l
#     else:
#         ns += ' '
# ns = ns.split()
# for i in ns[::-1]:
#     print(i, end=' ')

# s = "abbc"
# print(set(s))

