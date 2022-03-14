'''
中秋节公司分月饼，m个员工，买了n个月饼，m<=n，每个员工至少分1个月饼，但可以分多个。
单人份到最多月饼的个数为Max1，单人分到第二多月饼的个数是Max2，Max1-Max2<=3。
单人分到第n-1多月饼的个数是Max(n-1)，单人分到第n多月饼的个数是Max(n)，Max(n-1)-Max(n)<=3。
问有多少种分月饼的方法？
'''


def distribute(m, p, k):
    # m为待分配的人数, p为剩余的月饼
    # 在剩余的月饼中，假设第一个人总是分到最少，为k个
    if m <= 0 or p <= 0:
        # 人数为0或月饼数少于人数, 有0种分配方案
        return 0

    if m == 1:
        if k <= p <= k + 3:
            # 两人时, 第一人已经分到k个, 第二人要分的月饼在[k, k+3]之间, 则为1种有效方案
            return 1
        else:
            return 0

    cnt = 0
    for i in range(k, k + 4):  # k取不同值时的分配方案
        cnt += distribute(m - 1, p - i, i)
    return cnt


def mooncake(m, n):
    p = n - m
    cnt = 0
    i = 0
    while i <= p:
        cnt += distribute(m - 1, p - i, i)
        i += 1
    return cnt


print(mooncake(6, 12))
