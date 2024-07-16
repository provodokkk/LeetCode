# Time Complexity: O(n)

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r = []
        for i in nums:
            if r and i - 1 == r[-1][-1]:
                r[-1].extend([i])
            else:
                r.append([i])

        return [f'{i[-1]}' if len(i) == 1 else f'{i[0]}->{i[-1]}' for i in r]
        