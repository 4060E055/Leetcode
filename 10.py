# Q:Regular Expression 「*」 & 「.」

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        for i in range(len(s)):
            n, TF = Solution.Match(i, n)

        return TF

    def Match(self, sn, pn):
        n = 0
        patten = p[n]
        if patten == "*" and i != p[n - 1]:  # 是* 但是下一個不重複(因可能為0個)
            n += 1
            patten = p[n]




        elif patten != "." and patten != i:  # 不是. 跟比對不同
            return 0,False


        else:
            n += 1
            if patten == "*": n -= 1
            if n > len(p): return 0,False
        return n,True

    # 1 F   2 T   3 T     4 F           5 F     6T           7 F    8 F  9T  10F     11 T  12 T
s = ["aa", "aa", "ab", "ahiuhljlj", "afdfssfq", "aab","mississippi","ab","ab","aaa","aaa","aaa"]
p = ["a", "a*", ".*", "a*.j", "a*.fg", "c*a*b","mis*is*p*.",".*c",".*","aaaa","a*a","ab*a*c*a"]
ans = Solution()
nn = 0
for i, y in zip(s, p):
    nn += 1
    print(nn, ans.isMatch(i, y))
