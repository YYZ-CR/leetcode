from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[i]-nums[i+1]) for i in range(-1,len(nums)-1))

        