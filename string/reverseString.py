"""
翻转字符串
"""
s = "abcdef"
def reverseString01(s: str) -> str:
    """
    切片
    :param s:
    :return:
    """
    return s[::-1]

def reverseString02(s: str) -> str:
    """
    使用双指针
    :param s:
    :return:
    """
    t = list(s)
    n = len(t)
    left, right = 0, n-1
    for i in range(n):
        if left < right:
            t[left], t[right] = t[right], t[left]
            left += 1
            right -= 1
    return "".join(t)

print(reverseString02(s))