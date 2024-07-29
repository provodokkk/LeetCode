# Time Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        chars = set()
        left = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
