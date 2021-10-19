"""
字符串第一个唯一字符
"""
from collections import Counter, deque

s = "leetccooddel"

def firstUniqChar01(s: str) -> int:
    """
    使用哈希表存储索引
    :param s:
    :return:
    """
    dic = {}
    for index,ch in enumerate(s):
        if ch not in dic:
            dic[ch] = index
        else:
            dic[ch] = -1
    n = first = len(s)
    for index in dic.values():
        if index != -1 and index < first:
            first = index
    return -1 if first == n else first

def firstUniqChar02(s: str) -> int:
    """
    使用哈希表存储频数
    :param s:
    :return:
    """
    frequency = Counter(s)
    for index, ch in enumerate(s):
        if frequency[ch] == 1:
            return index
    return -1

def firstUniqChar03(s: str) -> int:
    """
    使用队列
    队列具有先进先出的性质
    维护队列时，使用了延迟删除这一技巧，即使队列中有一些字符出现超过了一次，但不位于队首，
    不造成影响，可以不删除
    :param s:
    :return:
    """
    queue = deque()
    dic = {}
    for index, ch in enumerate(s):
        if ch not in dic:
            dic[ch] = index
            queue.append((ch, index))
        else:
            dic[ch] = -1
            while queue and dic[queue[0][0]] == -1:
                queue.popleft()
    return queue[0][1] if queue else -1


print(firstUniqChar03(s))