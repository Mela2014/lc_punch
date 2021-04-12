class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        presum = 0
        snode = ListNode(0, head)
        maps = collections.OrderedDict()
        curr = snode
        while curr:
            presum += curr.val
            prev = curr
            if presum in maps:
                prev = maps[presum]
                prev.next = curr.next
                while presum in maps:
                    maps.popitem()
            maps[presum] = prev
            curr = curr.next
        return snode.next
