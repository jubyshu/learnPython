# 最大公约数
# def gcd(a, b):
#     return a if b == 0 else gcd(b, a % b)
#
# # 最小公倍数
# def lcm(a, b):
#     return a * b / gcd(a, b)
#
# s = input().split()
#
# a = int(s[0])
# b = int(s[1])
# print(gcd(a, b))
# print(int(lcm(a, b)))

# def lcm2(a, b):
#     if a < b:
#         a, b = b, a
#     for i in range(a, a * b + 1, a):
#         if i % b == 0:
#             print(i)
#             break
#
# lcm2(12, 18)

# a, b = list(map(int, input().split()))
# print(a)
# print(b)

# eval 函数
# s = '3+2*{1+2*[-4/(8-6)+7]}'
# s = s.replace('{', '(')
# s = s.replace('}', ')')
# s = s.replace('[', '(')
# s = s.replace(']', ')')
# print(int(eval(s)))

s = '1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\]['
a = 0
b = 0
c = 0
d = 0
for i in s:
    if i.isalpha():
        a += 1
    elif i.isspace():
        b += 1
    elif i.isdecimal():
        c += 1
    else:
        d += 1
print(a)
print(b)
print(c)
print(d)