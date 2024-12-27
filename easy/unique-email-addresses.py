# Time Complexity: O(n * k)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            email = emails[i]
            name, domain = email.split('@')
            name = name.split('+')[0]
            name = name.replace('.', '')
            emails[i] = name + '@' + domain

        return len(set(emails))
