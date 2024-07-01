# Time Complexity: O(log(n))

from math import ceil

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original_x = x
        reversed_x = 0

        while x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        return reversed_x == original_x
