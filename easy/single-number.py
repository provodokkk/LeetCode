# Time Complexity: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        element_count = {}
        for i in nums:
            if i in element_count:
                element_count[i] = 2
            else:
                element_count[i] = 1

        for key in element_count:
            if element_count[key] == 1:
                return key
        