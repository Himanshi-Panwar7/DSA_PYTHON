class Solution:
    def largest_secondlargest(self,nums: list[int]) -> tuple[int,int]:
        largest= float('-inf')
        second_largest=float('inf')
        if len(nums)< 2:
            return (-1,-1)
        for i in nums:
            if i> largest:
                second_largest=largest
                largest=i
            elif i>second_largest and i<largest:
                second_largest=i
        if second_largest== '-inf':
            return(largest,-1)
        return(largest,second_largest)
        