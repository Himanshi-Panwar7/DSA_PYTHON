class Solution:
    def cumulativefrequecy(self,nums: list[int]) -> list[int]:
        output=[]
        right_sum= sum(nums)
        left_sum=nums[0]
        for index,i in enumerate(nums):
            if index==0:
                output.append(i)
            else:
             left_sum+= i
             output.append(left_sum)
        return output
    
if __name__ == "__main__":
     user_input = input()
     nums = [int(x) for x in user_input.split()]
     sol = Solution()
     result = sol.cumulativefrequecy(nums)
     print(result)

