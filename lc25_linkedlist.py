# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        snode = left = right = ListNode(next = head)
        while right:
            for _ in range(k):
                if right: right = right.next
                else: break
            if not right: break
            prev, curr, mark = right.next , left.next, left.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            left.next = prev
            left = right = mark

        return snode.next
