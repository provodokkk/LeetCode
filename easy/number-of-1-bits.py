# Time Complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(32):
            cnt += n & 1
            n >>= 1

        return cnt
        