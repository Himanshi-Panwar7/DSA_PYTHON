# from collections import defaultdict
# import heapq
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         mapping=defaultdict(int)
#         for i in nums:
#             mapping[i]+=1    thsi take nlogn
#         return heapq.nlargest(k,mapping.keys(),key=mapping.get)
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mapping=defaultdict(int)
        output=[]
        for i in nums:
            mapping[i]+=1
        frequency= [[] for i in range(len(nums)+1)]
        for num , count in mapping.items():
            frequency[count].append(num)
        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                output.append(num)
                if len(output)==k:
                    return output # thsi take n  and is bucket sort
