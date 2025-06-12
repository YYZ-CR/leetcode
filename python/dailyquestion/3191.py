class Solution:
    def minOperations(self, nums: list[int]) -> int:
        counter = 0
        for i in range(len(nums)-2):
            if nums[i] != 1:
                nums[i], nums[i+1], nums[i+2] = 1-nums[i], 1-nums[i+1], 1-nums[i+2]
                counter += 1   
        if nums[-1] != 1 or nums[-2] != 1:
            return -1
        return counter