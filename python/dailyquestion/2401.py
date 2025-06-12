class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        longest = 1
        current = [nums[0]]
        for i in range(len(nums)-1):
            if (nums[i] & nums[i+1]) == 0:
                current.append(nums[i+1])
                for j in current[:-1]:
                    if (j & nums[i+1]) != 0:
                        current.remove(j)
            else: 
                current = [nums[i+1]]
            longest = max(longest,len(current))
        return longest
    
    #83ms   