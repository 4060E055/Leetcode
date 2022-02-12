
# algorithm：Single linked list
# linked list's url：https://www.bilibili.com/s/video/BV167411G7ya
# method:個十百...取，每取一個乘上對應的位數(10**i)，把以上加總後轉化字串翻轉逐一存入linked list(存入前會轉回int)



# Detailed answer

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ----------check example
# l1 = [2, 4, 9]
#
# l2 = [5, 6, 4, 9]
#
#
# class Solution(object):
#     @classmethod
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         self.l1 = l1
#         self.l2 = l2
#
#         sum = 0
#
#         for i in range(len(self.l1)):
#             # sum += self.l1[i] * (10 ** (len(self.l1) - (i + 1)))
#             sum += self.l1[i] * (10 ** (i))
#
#         for i in range(len(self.l2)):
#             # sum += self.l2[i] * (10 ** (len(self.l2) - (i + 1)))
#             sum += self.l2[i] * (10 ** (i))
#
#         ans = []
#         for i in str(sum):
#             ans.append(int(i))
#         return ans[::-1]
#
#
# print(Solution.addTwoNumbers(l1, l2))

# ------------ans---------------
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#
#         a1 = []
#         b1 = []
#
#         # get Single linked list and chenge to list
#         while l1 is not None:
#             a1.append(l1.val)
#             l1 = l1.next
#
#         while l2 is not None:
#             b1.append(l2.val)
#             l2 = l2.next
#
#         sum = 0
#
#         for i in range(len(a1)):
#             sum += a1[i] * (10 ** i)
#
#         for i in range(len(b1)):
#             sum += b1[i] * (10 ** i)
#
#         ans = []
#
#         for i in str(sum):
#             ans.append(int(i))
#
#         # print(ans[:: ]
#
#         for i in range(len(ans) - 1, -1, -1):
#             if i == len(ans) - 1:
#                 p = ListNode(ans[i])  # 開頭
#                 ans2 = p
#             else:
#                 p.next = ListNode(ans[i])  # 開頭的下一個next 指向
#                 p.next.val
#                 p = p.next
#                 p.val
#
#
#         # show linked liset  all val
#         #         while ans2 is not None:
#         #             print(ans2.val,end=",")
#         #             ans2=ans2.next
#
#         return ans2

# --------------------Optimization answer-------------
# 合併for and list

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#
#         sum = 0
#         n = 0
#         while l1 is not None:
#             sum += l1.val * (10 ** n)
#             l1 = l1.next
#             n += 1
#
#         n = 0
#         while l2 is not None:
#             sum += l2.val * (10 ** n)
#             l2 = l2.next
#             n += 1
#
#         n = 0
#         for i in str(sum)[::-1]:
#             if n == 0:
#                 p = ListNode(int(i))
#                 ans2 = p
#             else:
#                 p.next = ListNode(int(i))
#                 p = p.next
#             n += 1
#
#         return ans2
