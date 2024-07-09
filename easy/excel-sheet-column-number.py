# Time Complexity: O(n * log(n))

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        A = ord('A')
        res = 0

        for i, ch in enumerate(columnTitle[::-1]):
            res += (ord(ch) - A + 1) * pow(26, i)
                    
        return res
        