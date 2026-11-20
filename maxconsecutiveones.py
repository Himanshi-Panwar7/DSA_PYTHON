class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current_count=0
        max_count=0
        for _ in nums:
            if _!=0:
                current_count+=1
                max_count= max(current_count,max_count)
            else:
                current_count =0