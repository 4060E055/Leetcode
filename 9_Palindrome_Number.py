# Q:判斷數值轉為字串後是否為回文

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        if string == string[::-1]:
            return True
        else:
            False
