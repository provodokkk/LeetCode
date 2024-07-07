# Time Complexity: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length = 0
        for ch in s[::-1]:
            if length == 0 and ch != ' ':
                length += 1
            elif length != 0 and ch == ' ':
                return length
            elif ch != ' ':
                length += 1

        return length
