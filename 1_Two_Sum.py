# algorithm：none
# method：利用target逐一減nums的值，如果減完過後的值存在於nums裡，且兩者索引不同，則為答案
from typing import List

# nums = [3, 3]
# target = 6
#
# ans = [-1, -1]
# for index, value in enumerate(nums):
#     if target - value in nums:
#         ans[0] = index
#
#         ans[1] = nums.index(target - value)
#         if ans[0] != ans[1]:
#             break
#
# print(sorted(ans))  # output

# ---------------ans--------------

# input list int
# output list

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ans = [-1, -1]
#         for index, value in enumerate(nums):
#                 if target - value in nums:
#                     ans[0] = index
#                     ans[1] = nums.index(target - value)
#                     if ans[0] != ans[1]:
#                         break
#         return sorted(ans)


# ------------other optimization answer-------------------
# add ：減完之後比對該index以後的所有value

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for idx, value in enumerate(nums):
#             if target - value in nums[idx + 1:]:
#                 return ([idx, nums.index(target - value,idx + 1)])

# -----------上下差不多，上面還是稍快一點點， 只差有沒有用enumerate()-------------------------

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         index = 0
#         for value in nums:
#             if target - value in nums[index + 1:]: #減完之後比對該index以後的所有value
#                 return ([index, nums.index(target - value, index + 1)])
#             index += 1


#-----------------------more firest answer-------------------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff={}
        for idx,num in enumerate(nums):
            if diff.get(num,None)==None:
                diff[target-num]=idx
            else:
                return [diff[num],idx]
