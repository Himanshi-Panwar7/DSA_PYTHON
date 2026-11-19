class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefix={0:1}
        current_sum=0
        for num in nums:
            current_sum+= num
            target_sum=current_sum-k
            if target_sum in prefix.keys():
                count +=prefix[target_sum]
            prefix[current_sum]=prefix.get(current_sum,0)+1
        return count