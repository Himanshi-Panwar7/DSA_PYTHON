class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        i=0
        for j in range(1,n):
            if nums[j] !=0 and nums[i]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            elif nums[i]!=0:
                i+=1
        return nums
    
if __name__ == "__main__":
    user_input = input()
    nums = [int(x) for x in user_input.split()]
    sol = Solution()
    result = sol.moveZeroes(nums)
    print(result)