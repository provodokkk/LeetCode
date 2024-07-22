# Time Complexity: O(m + n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(nums1), set(nums2)
        return [i for i in s1 if i in s2]
