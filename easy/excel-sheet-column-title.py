# Time Complexity: O(log(n))

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet_length = 26
        letters = []

        while 0 < columnNumber:
            letters.append(chr(ord('A') + (columnNumber - 1) % alphabet_length))
            columnNumber = (columnNumber - 1) // alphabet_length
        return ''.join(letters[::-1])
