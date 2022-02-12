# # method=Manacher’s Algorithm
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         ans = ""
#
#         for i in range(len(s)):
#             next_num = s.rfind(s[i], i + 1)
#
#             while next_num != -1:
#
#                 ss = s[i:next_num + 1]  # 取i~next_num範圍的s字串，+1才能取到next_num
#                 if len(ss) <= len(ans): break  # 小於等於答案就不繼續進行
#                 if ss == ss[::-1]:  # 比對反轉字串是否為回文
#                     ans = ss
#                     break
#                 next_num = s.rfind(s[i], i + 1, next_num)  # 查找位置直到next_num-1的位置(next_num該位置不會被查找)
#
#         if ans == "":
#             return s[0:1]
#
#         return ans
#
#
# s = ["", "ab", "cbbd", "efababadfa", "aacabdkacaa", "abbcccbbbcaaccbababcbcabca", "aaabaaaa"]
#
# _ans = Solution()
# nn = 0
# for i in s:
#     nn += 1
#
#     print(nn, _ans.longestPalindrome(i))
#
#
# # ----------------------optimazation -----------------

class Solution:
    def longestPalindrome(self, s: str) -> str:

        r = 0
        n = 0
        ans = ""

        for i in range(len(s) + 1):

            ss = s[i - r:i + 1]
            # print("\t", i - r, i + 1, ss)
            if (i - r) >= 0 and ss == ss[::-1]:
                if len(ss) > len(ans): ans = ss
                r += 2
                continue

            ss = s[i - n:i]
            # print("\t", i - n, i, ss)
            if (i - n) >= 0 and ss == ss[::-1]:
                if len(ss) > len(ans): ans = ss
                n += 2
                continue

        return ans


#    1    2 a   3 bb    4 bb    5ababa       6 aca             7 bbcccbb    cbababc      8 aaabaaa  9 aaabaaa  10 cc
s = ["", "ab", "abb", "cbbd", "efababadfa", "aacabdkacaa", "abbcccbbbcaaccbababcbcabca", "aaabaaaa", "aaaabaaa", "ccd"]
# s = ["aaabaaaa"]
a = "fdfwfwfw"
# print(a[0:2])

_ans = Solution()
nn = 0
for i in s:
    nn += 1

    print(nn, _ans.longestPalindrome(i))


# ----------------------optimazation fastest-----------------

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if s == s[::-1]:
            return s

        longest_start = 0
        longest_length = 1

        for i in range(1, n):
            end = i + 1

            start = end - (longest_length + 2)
            substring = s[start:end]
            if start >= 0 and substring == substring[::-1]:
                longest_start = start
                longest_length += 2
                continue

            start = end - (longest_length + 1)
            substring = s[start:end]
            if start >= 0 and substring == substring[::-1]:
                longest_start = start
                longest_length += 1
                continue

        return s[longest_start:longest_start + longest_length]
