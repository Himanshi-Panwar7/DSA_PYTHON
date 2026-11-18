class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        look= set(nums)
        longest_streak=0
        for i in look:
            if (i-1) not in look:
                current_num=i
                current_count=1
                while(current_num+1 in look):
                 current_num+=1
                 current_count+=1
                longest_streak=max(longest_streak,current_count)
        return longest_streak
