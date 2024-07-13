# Time Complexity: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return 0
        return not (n & n-1)
