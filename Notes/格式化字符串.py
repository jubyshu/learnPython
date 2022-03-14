# 格式化字符串的三种方式

# --------- % 操作符 ------------
s = "I'm %s, I'm %.1f." % ('Mi Ki Hiro', 27.8)
print(s)

# >>> 指定最小输出宽度
# 对于整数和字符串，当数据的实际宽度小于指定宽度时，会在左侧以空格补齐
s1 = 'I like %10s.' % 'apple'
print(s1)

# >>> 指定对齐方式
# -: 左对齐, +: 输出的数字带正负符号, 0:宽度不足时补0
s2 = 'I have %-+05f apples.' % 5.6
print(s2)

# >>> 指定小数精度
# 精度值需要放在最小宽度之后，中间用点号隔开
s3 = 'I have %10.3f dreams.' % 3.1415926
print(s3)

# --------- format 方法 ------------
Me = {
    'Lname': 'Mi',
    'Mname': 'Ki',
    'Fname': 'Hiro'
}

print('He is {0[Lname]} {0[Mname]} {0[Fname]}'.format(Me))

# --------- f-string ------------
book = 'On the Road'
print(f'I like {book}')