# Time Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                return False

        return True
