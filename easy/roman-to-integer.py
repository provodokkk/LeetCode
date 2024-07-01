# Time Complexity: O(n)

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        n = len(s)

        for i in range(n):
            if i + 1 < n and symbol_value[s[i]] < symbol_value[s[i + 1]]:
                result -= symbol_value[s[i]]
            else:
                result += symbol_value[s[i]]

        return result
        