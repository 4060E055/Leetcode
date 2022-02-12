from typing import List


# method:取規律放進的波段(波封到波谷的概念) 然後再依序排列補齊空白放進

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows > 1:
#             str1 = []
#             str2 = []
#             n = 0
#             for i in range(len(s) + 1):  # 波段取  str2中間的分開取
#                 if (i % ((numRows - 1) * 2) == 0) and i != 0:
#                     str1.append(s[n:numRows + n])
#                     str2.append(s[numRows + n:i])
#                     # print("i",i)
#                     n = i
#
#             if len(s[n:]) <= numRows:
#                 str1.append(s[n:] + " " * (numRows - len(s[n:])))
#             else:
#                 str1.append(s[n:n + numRows] + " " * (numRows - len(s[n:]) + 1))  # 補齊str1的尾端空白
#                 # str2.append(s[n + numRows:] + " " * (numRows - 2 - len(s[n + numRows:])))
#                 str2.append(s[n + numRows:])
#
#             for i in range(len(str2)):  # 補齊空白在反向
#                 str2[i] = (" " + str2[i] + (" " * (len(str1[0]) - len(str2[i]) - 1)))[::-1]
#
#             q = []
#             for i in range(len(str1) + len(str2)):
#                 # print(i)
#                 if i % 2 == 0:
#                     q.append(str1[i // 2])
#                 else:
#                     q.append(str2[i // 2])
#
#             # for i in q:
#             #     print(i)
#
#             ans = ""
#             for i in str1:
#                 print("str1", list(i))
#             for i in str2:
#                 print("str2", list(i))
#
#             for i in range(numRows):  # 0 1 2 3
#                 for j in range(len(q)):
#                     ans += q[j][i]
#
#             return ans.replace(" ", "")
#             # return ans
#         else:
#             return s
#
#
# # s = "ABCD"
# s = "PAYPALISHIRING"
#
# numRows =3
# ans = Solution()
#
# print("ans=", ans.convert(s, numRows))
#
# print("PAHNAPLSIIGYIR")#3
# # print("PINALSIGYAHRPI")#4
# # print("PHASIYIRPLIGAN")  # 5
#

# --------------ans-------------------
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows <= 1 or len(s)<=2: return s
#         str1 = []
#         str2 = []
#         n = 0
#         for i in range(len(s) + 1):
#             if (i % ((numRows - 1) * 2) == 0) and i != 0:
#                 str1.append(s[n:numRows + n])
#                 str2.append(s[numRows + n:i])
#                 n = i
#         if len(s[n:]) <= numRows:
#             str1.append(s[n:] + " " * (numRows - len(s[n:])))
#         else:
#             str1.append(s[n:n + numRows] + " " * (numRows - len(s[n:]) + 1))
#
#             str2.append(s[n + numRows:])
#
#         for i in range(len(str2)):
#             str2[i] = (" " + str2[i] + (" " * (len(str1[0]) - len(str2[i]) - 1)))[::-1]
#
#         q = []
#
#         for i in range(len(str1) + len(str2)):
#             if i % 2 == 0:
#                 q.append(str1[i // 2])
#             else:
#                 q.append(str2[i // 2])
#
#         ans = ""
#
#         for i in range(numRows):
#             for j in range(len(q)):
#                 ans += q[j][i]
#
#         return ans.replace(" ", "")


# -----------Other ans. Optimization?---------------較簡潔，但速度跟記憶體沒差
# method:區分numRows區塊，按照0~numRows-1的順序逐一放入numRows對應區塊中，最後連結區塊輸出ans
# if numRows=4: 0 1 2 3 2 1 0 (Z字形來回)

# from functools import reduce
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # rows = ["" for _ in range(numRows)]  # for _ in   == 起到循環作用，但不會用到參數
        rows = [""] * numRows  # 兩種做法效率幾乎一樣
        n = 0
        d = 1
        if numRows <= 1 or len(s) <= 2:
            return s

        for i in s:
            # print(n)# if numRows=4: 0 1 2 3 2 1 0
            rows[n] += i
            # print(n)
            n = n + d
            if n >= numRows - 1 or n <= 0:
                d *= -1
        # print(rows)
        return "".join(rows)
        # return reduce(lambda x, y: x + y, rows)  # 上下兩者return方法差不多，差在這個要import而已


numRows = 3
s = "PAYPALISHIRING"
ans = Solution()
print(ans.convert(s, numRows))
