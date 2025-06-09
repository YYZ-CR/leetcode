class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        istrue = True
        while istrue and len(nums) > 0:
            value = nums.pop(0)
            istrue = value in nums
            if istrue: nums.remove(value)
        return istrue