# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        snode = ListNode(0, head)
        left = snode
        for _ in range(m-1):
            left = left.next
        right = left.next
        for _ in range(n-m):
            pre = right
            right = right.next

            pre.next = right.next
            right.next = left.next
            left.next = right
            right = pre
        return snode.next
