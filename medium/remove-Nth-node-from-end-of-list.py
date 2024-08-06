# Time Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def remove_node(node: Optional[ListNode]) -> int:
            if not node:
                return 0
            
            index = remove_node(node.next) + 1
            if index == n + 1:
                node.next = node.next.next

            return index

        dummy = ListNode(next=head)
        remove_node(dummy)
        return dummy.next
