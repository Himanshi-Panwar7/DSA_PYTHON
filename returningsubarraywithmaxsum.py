class Solution:
    def maxSubArray(self, nums: list[int]) -> list[int]:
        current_sum =nums[0]
        start_index=0
        end_index=0
        max_sum=nums[0]
        for index,num in enumerate(nums):
            if index==0:
                continue
            if current_sum+num<num:
                start_index=index
            current_sum=max(current_sum+num,num)
            if max_sum<current_sum:
                end_index=index
            max_sum=max(current_sum, max_sum)

        return nums[start_index:end_index+1]

if __name__ =="__main__":
    lists= input()
    lists= [int(x) for x in lists.split()]
    obj1= Solution()
    output= obj1.maxSubArray(lists)
    print(output)