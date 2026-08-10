class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for ch in haystack:
        #     if ch == needle[0]:

        # pass
        # i = 0
        # ch = haystack[i]
        # while ch:
        #     if ch == needle[0]:
        #         for j in range(len(needle)):
        #             if not (heystack[i+j] == needle[j]):
        #                 i += j

        if needle == "":
            return 0

        lps = [0] * len(needle)

        length = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j

            elif j > 0:
                j = lps[j - 1]

            else:
                i += 1

        return -1



# 已经匹配的信息没有利用
#

if __name__ == "__main__":
    s1 = Solution()
    print(s1.strStr("sadbutsad", "sad"))    # 0
    print(s1.strStr("leetcode", "leeto"))   # -1
    print(s1.strStr("mississippi", "issip"))  # 4
    print(s1.strStr("hello", ""))          # 0
