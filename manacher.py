# 字符串中的最长回文字符串
def manacher(s):
    # 字符串预处理
    s = '#' + '#'.join(s) + '#'

    radius = [0] * len(s)  # 以每个字符串为中心的回文半径
    max_right = 0  # 已知回文串半径的最右边界
    circle = 0  # 回文串的中心
    max_len = 0

    for i in range(len(s)):
        # 确定第i个字符的回文半径
        if i < max_right:
            radius[i] = min(radius[2 * circle - i], max_right - i)
        else:
            radius[i] = 1
        # 由第i个字符向两侧拓展回文串
        # i - radius[i] >= 0 左侧还可以拓展
        # i + radius[i] < len(s) 右侧不能超过
        while i - radius[i] >= 0 and i + radius[i] < len(s) and s[i - radius[i]] == s[i + radius[i]]:
            radius[i] += 1
        # 回文串的长度与最右边界对比
        # 更新最右边界及其中心
        if radius[i] + i - 1 > max_right:
            max_right = radius[i] + i - 1
            circle = i
        # 更新最大回文长度
        # 回文半径-1即为原始字符串的回文长度
        max_len = max(max_len, radius[i])
    return max_len - 1


print(manacher('abba'))
