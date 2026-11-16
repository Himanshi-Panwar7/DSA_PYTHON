#here I made mistake of using teh set but it change the order of occurernce of number also there was need to make an extra array given taht array is sorted
class Solution:
 def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
         return -1
        i=0
        for j in range(1,len(nums)):
            if nums[i] !=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1