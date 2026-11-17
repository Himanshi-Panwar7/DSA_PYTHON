class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            current_target=target-nums[i]
            if current_target in seen:
                return [seen[current_target],i]
            else:
                seen[nums[i]]=i