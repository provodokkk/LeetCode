# Time Complexity: O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def extractPalindrome(i: int, is_even: bool) -> None:
            left, right = i, i + int(is_even)
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1

            if len(self.result) < right - left - 1:
                self.result = s[left + 1:right]

        self.result = ''
        for i in range(len(s)):
            extractPalindrome(i, True)
            extractPalindrome(i, False)

        return self.result
