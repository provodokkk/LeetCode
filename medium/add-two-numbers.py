# Time Complexity: O(m + n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.get_num(l1)
        num2 = self.get_num(l2)
        sum = num1 + num2

        dummy_head = ListNode()
        current = dummy_head

        while sum > 0:
            current.next = ListNode(val=sum % 10)
            sum //= 10
            current = current.next
        
        return dummy_head.next if dummy_head.next else dummy_head


    def get_num(self, l: Optional[ListNode]):
        num = 0
        power = 1
        while l:
            num += l.val * power
            l = l.next
            power *= 10
        return num
