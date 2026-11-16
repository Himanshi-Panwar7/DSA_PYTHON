# This was my appraoch of doing here I learning
# but here the time complexity incresed
# because every time n elements are copied k time which excceded tiem limit
# also list slicing require extra space it do the we need to write[:]
# class Solution:
#     def rotate(self, nums: list[int], k: int) -> list[int]:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for _ in range(k):
#             nums=nums[-1:]+ nums[:-1]
#         return nums

# here I adopted the two pointer approach
# The two-pointer approach is an algorithmic pattern that uses two index 
# variables (pointers) to traverse a linear data structure—such 
# as an array, string, or linked list—in a coordinated way. Instead of using nested loops that check every 
# possible pair in $O(n^2)$ time, two pointers reduce time complexity to $O(n)$ while using $O(1)$ extra memory



class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==0:
            return
        k%=n
        def reverse(l:int,r:int)->None:
            while l<r:
                nums[l], nums[r] = nums[r],nums[l]# tuple unpacking in python 
                l+=1
                r-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        
        
if __name__ == "__main__":
    k= input()
    user_input = input()
    nums = [int(x) for x in user_input.split()]
    sol = Solution()
    result = sol.rotate(nums,int(k))
    print(result)

        