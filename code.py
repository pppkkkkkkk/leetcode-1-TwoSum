class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in dict:
                return [dict[nums[i]],i]
            dict[diff] = i
        
            