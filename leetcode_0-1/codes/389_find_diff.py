from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((Counter(t) - Counter(s)).keys())[0]

s = "abcd"
t = "abcde"
print(list((Counter(t) - Counter(s)).keys())[0])
print(Counter(t))
print((Counter(t) - Counter(s)))
print(list((Counter(t) - Counter(s))))


# 另一种更直观的解法
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # a, b = 0, 0
        # for ch in s:
        #     a += ord(ch)
        # for ch in t:
        #     b += ord(ch)
        # return chr(b - a)

        d1 = {}
        for ch in s:
            d1[ch] = d1.get(ch, 0) + 1
        for ch in t:
            d1[ch] = d1.get(ch, 0) - 1
        for key, val in d1.items():
            if val == -1:
                return key

# 最优解：异或
# 异或是一种“消除重复”的运算
# a ^ a = 0
# a ^ 0 = a
# a^b^c = a^c^b
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for c in s + t:
            result ^= ord(c)
        return chr(result)
