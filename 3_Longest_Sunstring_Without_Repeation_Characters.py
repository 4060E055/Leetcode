# algorithm:
# Substring vs Subsequence's url:
# https://m41045.pixnet.net/blog/post/278834088-substring-%E8%88%87-subsequence-%E5%B7%AE%E7%95%B0
# longest substring's url:
# http://web.ntnu.edu.tw/~algo/Substring4.html#3
# exercise :找出最長無重複字串
# method:逐一遍歷s 如果char(i)在word裡面 則取word裡char後的字串 在加上char本身，並計算len 取最大len
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        word = ""
        for i in s:
            if i in word:
                word = word[word.index(i) + 1:] + i  # 較快一點
                # word = word[word.find(i) + 1:] + i
            else:
                word += i

            r = max(len(word), r)  # 較快一點
            # if len(word) > r: r = len(word)
            # if r == len(set(s)): return r #加這段可以減少一點memory使用(約0.2MB)，但會增加三倍Runtime
        return r


s = "dvdf"  # 3
# s = "pwwkew" #3
ans = Solution()
print(ans.lengthOfLongestSubstring(s))

#-------------------------ans----------------------------------
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         r = 0
#         word = ""
#         for i in s:
#             if i in word:
#                 word = word[word.index(i) + 1:] + i
#             else:
#                 word += i
#             r = max(len(word), r)
#         return r
