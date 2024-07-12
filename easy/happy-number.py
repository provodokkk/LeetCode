# Time Complexity: O(log(n))

class Solution:
    def isHappy(self, n: int) -> bool:
        encountered_nums = set()

        while n != 1 and n not in encountered_nums:
            encountered_nums.add(n)
            n = self.get_next(n)

        return n == 1
    
    def get_next(self, number: int) -> int:
        sum = 0
        while number:
            digit = number % 10
            sum += digit ** 2
            number //= 10
        return sum
