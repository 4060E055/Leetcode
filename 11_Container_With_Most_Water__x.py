from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_place = 0


        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                 max_place=max( max_place,min(height[i], height[j]) * (j - i))


        return max_place


if __name__=="__main__":

    # height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height =[1,1]
    new = Solution()
    print(new.maxArea(height))