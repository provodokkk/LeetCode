# Time Complexity: O(n * l)
# l - the average length of the strings


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = min(strs, key=len)

        for i, ch in enumerate(shortest_str):
            for str in strs:
                if str[i] != ch:
                    return str[:i]

        return shortest_str
    