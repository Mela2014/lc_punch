# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        rslt = self.head.val
        curr = self.head.next
        i = 1
        while curr:
            if random.randint(0, i) == 0:
                rslt = curr.val
            curr = curr.next
            i += 1
        return rslt



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
