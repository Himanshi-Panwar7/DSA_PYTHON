class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        current_max=nums[0]
        current_min=nums[0]
        max_prod=nums[0]
        for i,num in enumerate(nums):
            if i ==0:
                continue
            if num<0:
                current_max, current_min= current_min, current_max
            current_max = max(current_max*num, num)
            current_min = min(current_min*num, num)
            max_prod=max(current_max, max_prod)
        return max_prod
        