# 输出斐波那契数列的第n个数
def fibo(n):
    a, b = 1, 1
    if n == 1 | n == 2:
        print(1)
    else:
        for i in range(n - 2):
            a, b = b, a + b
        print(b)


fibo(9)


# 输出斐波那契数列
def fibo_array(n):
    a, b = 1, 1
    arr = [1]
    if n == 1:
        print(arr)
    elif n == 2:
        arr.append(1)
        print(arr)
    else:
        arr.append(1)
        for i in range(n - 2):
            a, b = b, a + b
            arr.append(b)
        print(arr)


fibo_array(9)
