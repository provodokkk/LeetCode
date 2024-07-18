# Time Complexity: O(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                nums[i - cnt] = nums[i]

        if cnt:  
            nums[-cnt:] = [0] * cnt
        