# Time Complexity: O(n)

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length, curr_length = 1, 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_length += 1
                max_length = max(max_length, curr_length)
            else:
                curr_length = 1

        return max_length
