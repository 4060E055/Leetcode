from typing import List


class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()

        digit = ""
        posi_naga = s[0:1]
        n = 1
        if posi_naga != "+" and posi_naga != "-":
            posi_naga = ""
            n = 0

        for i in s[n:]:
            if 48 <= ord(i) <= 57: #i.isdigit()
                digit += i
            else:
                break

        if digit == "": #如果沒有任何數字則回傳0
            return 0

        ans = int(posi_naga + digit)

        #超過範圍回傳極限值
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif ans < -2 ** 31:
            return -2 ** 31
        else:
            return ans


_str = "+-12"
# _str = "words and 987"
_str = "+"
_ans = Solution()
print(_ans.myAtoi(_str))
