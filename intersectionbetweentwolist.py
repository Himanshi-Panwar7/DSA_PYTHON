class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 =set(nums1)
        result= set()
        for i in nums2:
            if i in set1:
                result.add(i)
        return list(result)
