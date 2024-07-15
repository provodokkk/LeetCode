# Time Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        encountered_nums = set()
        for i in nums:
            if i in encountered_nums:
                return True

            encountered_nums.add(i)
        return False
