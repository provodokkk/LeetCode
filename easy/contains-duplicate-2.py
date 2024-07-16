# Time Complexity: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        encountered_nums = {}
        for i in range(len(nums)):
            if nums[i] in encountered_nums and abs(encountered_nums[nums[i]] - i) <= k:
                return True

            encountered_nums[nums[i]] = i

        return False
        