# Time Complexity: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0
        for i in range(32):
            reversed_bits = (reversed_bits << 1) | (n & 1)
            n >>= 1
        return reversed_bits
