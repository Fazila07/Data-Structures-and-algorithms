# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        startNode = dummy
        endNode = head
        index = 1
        
        # find startNode (node before left) and endNode (node after right)
        cur = head
        while cur:
            if index == left - 1:
                startNode = cur
            if index == right:
                endNode = cur.next
                break
            index += 1
            cur = cur.next
        
        self.reverse(startNode, endNode)
        return dummy.next

    def reverse(self, start: ListNode, end: ListNode) -> None:
        prev = start
        cur = start.next
        head = cur
        
        while cur != end:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        
        head.next = end
        start.next = prev