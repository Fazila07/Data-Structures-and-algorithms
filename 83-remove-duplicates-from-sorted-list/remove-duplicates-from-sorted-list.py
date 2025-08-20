# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n,p,t=None,None,head
        while t:
            p=t.next
            while p and p.val==t.val:
                n=p.next
                p.next=None
                p=n
            t.next=p
            t=t.next
        return head
        