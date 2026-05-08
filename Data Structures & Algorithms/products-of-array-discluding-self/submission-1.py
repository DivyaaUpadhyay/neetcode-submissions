class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        result = [1] * n

        # Prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Postfix products
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result  
        