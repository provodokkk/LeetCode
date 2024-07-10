# Time Complexity: O(n)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        word_to_pattern, pattern_to_word = {}, {}

        for i, word in enumerate(words):
            if word in word_to_pattern and word_to_pattern[word] != pattern[i]:
                return False
            if pattern[i] in pattern_to_word and pattern_to_word[pattern[i]] != word:
                return False

            word_to_pattern[word] = pattern[i]
            pattern_to_word[pattern[i]] = word

        return True
