# Time Complexity: O(n * log(n))

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            remainder = heapq.heappop(stones) - heapq.heappop(stones)
            if remainder != 0:
                heapq.heappush(stones, remainder)

        return -stones[0] if stones else 0
