# def code(string):
#     l1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     l2 = '22233344455566677778889999bcdefghijklmnopqrstuvwxyza0123456789'
#     res = ''
#     for i in string:
#         res += l2[l1.index(i)]
#     return res
#
# print(code(input()))

l = input().split('.')
s = str(bin(int(input())))
s = s.replace('0b', '').rjust(32, '0')
n = ''

for i in l:
    t = str(bin(int(i))).replace('0b', '')
    t = t.rjust(8, '0')
    n += t

m = []
for i in range(4):
    m.append(s[8 * i:8 * (i + 1):])

p = []
for i in m:
    p.append(str(int(i, 2)))

print(int(n, 2))
print('.'.join(p))
