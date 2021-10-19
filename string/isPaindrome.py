"""
给定一个字符串，验证是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写
isalnum()：如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False。如'aaa111'.isalnum()返回True
isalpha()：如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
"""

st = "2 1 raceecar12"

def isPaindrome(s: str) -> bool:
    if s == "":
        return True
    sg = "".join(ch.lower() for ch in s if ch.isalnum())
    print(sg)
    left, right = 0, len(sg)-1
    while left < right:
        if sg[left] != sg[right]:
            return False
        left += 1
        right -= 1
    return True

print(isPaindrome(st))