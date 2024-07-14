# Time Complexity: O(m + n)

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_hash, magazine_hash = defaultdict(int), defaultdict(int)

        for i in ransomNote:
            note_hash[i] += 1

        for j in magazine:
            # only if we encounter an element that is in note_hash
            if magazine_hash[j] < note_hash[j]:
                magazine_hash[j] += 1

            if note_hash == magazine_hash:
                return True

        return False
