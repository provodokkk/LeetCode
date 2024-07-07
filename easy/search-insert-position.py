# Time Complexity: O(log(n))

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            central_index = (left + right) // 2

            if nums[central_index] == target:
                return central_index
            elif nums[central_index] < target:
                left = central_index + 1
            elif nums[central_index] > target:
                right = central_index - 1

        return right + 1
