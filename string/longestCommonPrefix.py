"""
最长公共前缀
"""
from typing import List

def longestCommonPrefix01(strs: List[str]) -> str:
    """
    取一个单词s，和后面单词比较，看s与每个单词相同的最长公前缀
    find(str,beg=0,end=len(string))：检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，
    如果包含返回开始的索引值，否则返回-1。如’abca’.find(‘a’)返回0，’abca’.find(‘a’，1)返回3，’abca’.find(‘3’)返回-1
    :param s:
    :return:
    """
    if not strs:
        return ""
    res = strs[0]
    n, i = len(strs), 1
    while i < n:
        while strs[i].find(res) != 0:
            res = res[0:len(res)-1]
        i += 1
    return res

def longestCommonPrefix02(strs: List[str]) -> str:
    """
    按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同
    list.sort(key=None,reverse=False):对原列表进行排序。reverse=False升序，True降序,默认为False
    :param strs:
    :return:
    """
    if not strs:
        return ""
    strs.sort()
    a, b, res = strs[0], strs[-1], ""
    for i in range(len(a)):
        if i < len(b) and a[i] == b[i]:
            res += a[i]
        else:
            break
    return res

def longestCommonPrefix03(strs: List[str]) -> str:
    """
    zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    在列表、元组、字典、集合、数组前面加上*，打印的输出结果可以看出，这些数据结构中元素都被分成一个一个的独立元素
    *strs 输出 flower flow flight
    :param strs:
    :return:
    """
    res = ""
    for tmp in zip(*strs):
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    return res

strs = ["flower","flow","flight"]
print(longestCommonPrefix03(strs))