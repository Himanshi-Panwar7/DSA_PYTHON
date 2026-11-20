class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        left_products = [1] * n
        right_products = [1] * n
        output = [1] * n

        # 1. Fill left_products (moving left -> right)
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # 2. Fill right_products (moving right -> left)
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # 3. Multiply left and right together
        for i in range(n):
            output[i] = left_products[i] * right_products[i]

        return output