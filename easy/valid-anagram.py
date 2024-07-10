# Time Complexity: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s, set_t = set(s), set(t)

        if set_s != set_t:
            return False

        for i in set_s:
            if s.count(i) != t.count(i):
                return False
        
        return True
