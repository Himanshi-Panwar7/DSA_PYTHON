#this is the brute force techqnique which I used 
#class Solution:
   # def check(self, nums: list[int]) -> bool:
       # sort_list=sorted(nums)
       # test=[]
        #for i, value in enumerate(sort_list):
           # test=sort_list[i:]+sort_list[:i]
            #if test==nums:
                #return True
       # return False
# to check whether the array is roatated or not we just have to chech whether the array element is greater than former if this count is greater than one then the array was not sorted 
class Solution:
    def check(self, nums: list[int]) -> bool:
        flag=0
        n= len(nums)
        for i, value in enumerate(nums):
            if nums[i] > nums[(i+1)%n]:
                flag+=1
        if flag >1:
            return False
        else:
            return True
