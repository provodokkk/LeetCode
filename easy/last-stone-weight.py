# Time Complexity: O(n^2 * log(n))

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            remainder = stones.pop() - stones.pop()
            if remainder:
                stones.append(remainder)
        return stones[0] if stones else 0
