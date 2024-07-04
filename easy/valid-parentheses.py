# Time Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        allowed_symbols = set("()[]{}")
        opening_brackets = set("([{")
        closing_brackets = set(")]}")
        only_allowed_symbols = all(ch in allowed_symbols for ch in s)

        if not only_allowed_symbols or s[0] in closing_brackets or s[-1] in opening_brackets:
            return False

        parentheses_stack = []
        for ch in s:
            if ch in opening_brackets:
                parentheses_stack.append(ch)
            elif not parentheses_stack:
                return False
            else:
                opening_bracket = parentheses_stack.pop()
                if parentheses[opening_bracket] != ch:
                    return False

        return not parentheses_stack
