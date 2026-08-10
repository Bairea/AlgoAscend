# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         # for i in range(1, len(s)):
#         #     sub = s[:i]

#         i = 0
#         j = 1
#         while j < len(s):
#             if s[0] != s[j]:
#                 i = j
#                 j += 1
#             else:
#                 for k in range(i+1):
#                     if s[k] == s[j]:
#                         j += 1
#                     else:
#                         break
#         if len(s) % i != 0:
#             return False
#         return True

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        n = len(s)

        next = [0] * n

        j = 0

        for i in range(1, n):

            while j > 0 and s[i] != s[j]:
                j = next[j-1]

            if s[i] == s[j]:
                j += 1

            next[i] = j


        length = next[-1]
        print(next)

        return length != 0 and n % (n - length) == 0


if __name__ == "__main__":
    s = "abcabcabcabc"
    s = "abcababcababcab"
    s1 = Solution()
    print(s1.repeatedSubstringPattern(s))
