# 反轉數值


class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            str_x = str(x * -1)[::-1]
            ans = int("-" + str_x)
        else:
            str_x = str(x)[::-1]
            ans = int(str_x)

        if ans < (-2 ** 31) or ans > (2 ** 31 - 1):
            return 0
        return ans


x = -123
x = 1534236469
ans = Solution()
print(ans.reverse(x))

# --------------較快的ans----------------以下較快  原因不明???
# class Solution:
#     def reverse(self, x: int) -> int:
#
#         str_x = str(x)[::-1]
#
#         if x < 0:
#             ans = int("-" + str_x.replace("-", ""))
#         else:
#             ans = int(str_x)
#
#         if ans < (-2 ** 31) or ans > (2 ** 31 - 1):
#             return 0
#         return ans
