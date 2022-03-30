# bubble sort 冒泡排序
def bubble_sort(li):
    for i in range(len(li) - 1):  # 排 n-1 趟
        for j in range(len(li) - i - 1):  # 无序区
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


# 冒泡排序优化
def bubble_sort_opt(li):
    for i in range(len(li) - 1):  # 排 n-1 趟
        exchange = False
        for j in range(len(li) - i - 1):  # 无序区
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return


# 查找排序
def search_sort(li):
    for i in range(len(li) - 1):  # n-1 趟
        min_loc = i
        for j in range(i + 1, len(li)):  # 无序区
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


# 插入排序
def insert_sort(li):
    for i in range(1, len(li)):  # 待插入区
        temp = li[i]
        j = i - 1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp


# ------------------------------------- #

# 快速排序
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


# 堆排序
# 向下调整函数
def sift(li, low, high):  # low: 根结点, high: 最后一个节点
    i = low
    j = 2 * i + 1  # 左子节点
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


def heap_sort(li):
    n = len(li)
    # 建堆
    for i in range((n - 2) // 2, -1, -1):  # i: 调整部分根的下标
        sift(li, i, n - 1)
    for i in range(n - 1, -1, -1):  # i 指向最后一个位置
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)


s = [6, 4, 7, 1, 9, 3, 2, 5, 8]
# search_sort(s)
# bubble_sort_opt(s)
# insert_sort(s)
# quick_sort(s, 0, len(s) - 1)
heap_sort(s)
print(s)
