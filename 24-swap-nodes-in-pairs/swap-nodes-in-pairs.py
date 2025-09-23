# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while head and head.next:
            first = head
            second = head.next

        # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

        # Move pointers
            prev = first
            head = first.next

        return dummy.next
    # Utility function to create linked list from list
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Utility function to print linked list
    def print_linked_list(head):
        vals = []
        while head:
            vals.append(str(head.val))
            head = head.next
        print("->".join(vals))