# Time Complexity: O(n)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        min_product, max_product = 1, 1

        for num in nums:
            if num == 0:
                min_product, max_product = 1, 1

            tmp = num * max_product
            max_product = max(num, tmp, num * min_product)
            min_product = min(num, tmp, num * min_product)
            result = max(result, max_product)

        return result
