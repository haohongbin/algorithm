"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
"""
s = "abcdefg"
k = 8

def reverseStr(s: str, k: int) -> str:
    """
    反转每个下标从 2k 的倍数开始的，长度为 k 的子串。若该子串长度不足 k，则反转整个子串
    :param s:
    :param k:
    :return:
    """
    t = list(s)
    for i in range(0, len(t), 2*k):
        t[i: i+k] = reversed(t[i: i+k])

    return "".join(t)

print(reverseStr(s, k))