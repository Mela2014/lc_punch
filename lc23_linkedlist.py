# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        interval = 1
        n = len(lists)
        while interval < n:
            for i in range(0, n-interval, 2*interval):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]

    def merge2Lists(self, a, b):
        snode = curr = ListNode()
        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next
        if a:
            curr.next = a
        else:
            curr.next = b
        return snode.next
