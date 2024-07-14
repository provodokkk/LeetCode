# Time Complexity: O(n)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s) // 2
        for i in range(length):
            s[i], s[~i] = s[~i], s[i]
        