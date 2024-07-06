# Time Complexity: O(n * m)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        for i in range(haystack_length - needle_length + 1):
            if haystack[i] == needle[0] and haystack[i:i + needle_length] == needle:
                return i
        
        return -1
