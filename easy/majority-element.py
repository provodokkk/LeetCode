# Time Complexity: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = list(set(nums))
        counter = {el: 0 for el in elements}
        n = len(nums) // 2

        for i in nums:
            counter[i] += 1

            if counter[i] > n:
                return i
