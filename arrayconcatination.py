class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums*2

if __name__ == "__main__":
    user_input = input()
    nums = [int(x) for x in user_input.split()]
    sol = Solution()
    result = sol.getConcatenation(nums)