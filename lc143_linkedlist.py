# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next

        prev, curr = None, s.next
        s.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        a, b = head, prev
        while b:
            temp = a.next
            a.next = b
            a = temp

            temp = b.next
            b.next = a
            b = temp
        return 
