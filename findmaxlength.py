class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen={0:-1}
        running_length=0
        max_length=0
        for i, num in enumerate(nums):
            running_length +=1 if num==1 else -1
            if running_length in first_seen:
                length= i-first_seen[running_length]
                max_length=max(max_length,length)
            else:
                first_seen[running_length]=i
        return max_length
        