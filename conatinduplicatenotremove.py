#my
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
     n=len(nums)
     nums= list[set(nums)]
     n1 =len(nums)
     if n!=n1:
        return False
     else:
        return True
    #chatgpt approach
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False