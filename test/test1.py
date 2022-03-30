# 计算字符串最后一个单词的长度
s = input()
lst = s.split()
print(len(lst[-1]))

# 计算某字符出现次数
# s1 = 'AbCc_2C'
# s2 = 'c'
# a = 0
# for let in s1:
#     if let.lower() == s2.lower():
#         a += 1
# print(a)
# ----------------
s1 = input().lower()
s2 = input().lower()
print(s1.count(s2))

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
new_lst = set(lst)  # 利用集合去重
final_lst = sorted(list(new_lst))
for num in final_lst:
    print(num)

# 字符串分隔
while True:
    try:
        l = input()
        while len(l) > 0:
            print(l[:8].ljust(8, '0'))
            l = l[8:]
    except:
        break

while True:
    try:
        l = input()
        for i in range(0, len(l), 8):
            print('{0:0<8s}'.format(l[i:i+8]))
    except:
        break
