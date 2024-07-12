# Time Complexity: O(m + n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        checked_nodes = {}
        while headA:
            checked_nodes[headA] = True
            headA = headA.next

        while headB:
            if headB in checked_nodes:
                return headB
            headB = headB.next
            
        return None
