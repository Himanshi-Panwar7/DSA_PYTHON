# my idea but uses space n and tiem n
# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#        n= len(nums) 
#        count_list=[0]*(n+1)
#        for i in nums:
#         count_list[i] +=1
#        for j in range(len(count_list)):
#         if count_list[j] == 0:
#             return j# but there is  a more goode way where there is no space
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)
