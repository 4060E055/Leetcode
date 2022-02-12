# algorithm： binary search 二分搜尋法 O(log (m+n))
# Time Complexity's url：
# https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E8%AA%8D%E8%AD%98%E5%B8%B8%E8%A6%8B%E6%BC%94%E7%AE%97%E6%B3%95-%E4%B8%80-b46fece65ba5
# method：extend連結字串後，計算list長度是奇還偶(%2)，再利用此找出中位數(有兩個就相加/2)
# exercise：取連結list後的中位數
from typing import List

# def findMedianSortedArrays(nums1, nums2) -> float:
#     nums1.extend(nums2).sort()
#     n = len(nums1)
#     if n % 2 == 1:
#         return nums1[n // 2]  # 整數除法
#     else:
#         return (nums1[n // 2 - 1] + nums1[n // 2]) / 2.0
#
#
# # nums1.extend(nums2) #兩種連結方法
#
#
# nums1 = [1, 2]
# nums2 = [3, 4]


# ans = findMedianSortedArrays(nums1, nums2)
# print(ans)

# ---------------------ans--------------------------

nums1 = [1, 2]
nums2 = [3, 4]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n % 2 == 1:
            return nums1[n // 2]
        else:
            return (nums1[n // 2 - 1] + nums1[n // 2]) / 2.0


ans = Solution()
print(ans.findMedianSortedArrays(nums1, nums2))

# ----------------------optimazation-----------------
