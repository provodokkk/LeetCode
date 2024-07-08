# Time Complexity: O(log(x))

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x

        while left <= right:
            middle = (left + right) // 2
            divided = x // middle

            if middle > divided:
                right = middle - 1
            elif middle < divided:
                left = middle + 1
            else:
                return middle

        return left - 1
            