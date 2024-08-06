# Time Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = ListNode(next=head), ListNode(next=head)

        for i in range(n + 1):
            right = right.next

        if not right:
            return head.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return head
