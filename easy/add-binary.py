# Time Complexity: O(n)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        a = a.zfill(length)
        b = b.zfill(length)

        res = []
        k = 0
        for index in range(length -1, -1, -1):
            total = int(a[index]) + int(b[index]) + k

            res.append(str(total % 2))
            k = total // 2

        if k:
            res.append('1')


        return ''.join(reversed(res))
