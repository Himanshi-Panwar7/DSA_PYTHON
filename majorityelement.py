class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)/2
        seen={}
        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i],0)+1
        key= next(k for k, value in seen.items() if value>n)
        return key