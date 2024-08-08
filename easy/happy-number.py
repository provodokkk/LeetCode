# Time Complexity: O(log(n))

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getSquared(n: int) -> int:
            res = 0
            while n:
                res += (n % 10) ** 2
                n //= 10
            return res

        slow, fast = n, getSquared(n)
        while slow != fast:
            slow = getSquared(slow)
            fast = getSquared(getSquared(fast))

        return slow == 1
