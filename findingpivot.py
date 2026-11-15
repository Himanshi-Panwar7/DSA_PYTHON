class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right_sum = sum(nums)
        left_sum=0
        for index,value in enumerate(nums):
            right_sum -=value
            if right_sum==left_sum:
                return index
            left_sum+= value
        
        return -1