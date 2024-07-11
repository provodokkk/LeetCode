# Time Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        encountered_elements = {}
        while head:
            if head in encountered_elements:
                return True
            encountered_elements[head] = 1
            head = head.next

        return False
