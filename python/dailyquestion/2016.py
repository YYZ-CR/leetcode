class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = inf
        max_diff = 0
        for i in nums:
            if i < min_value:
                min_value = i
            if i - min_value > max_diff:
                max_diff = i - min_value          
        
        if max_diff == 0:
            return -1
        else: return max_diff
        