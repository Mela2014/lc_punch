class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1, temp2 = l1, l2
        while temp1 and temp2:
            temp1 = temp1.next
            temp2 = temp2.next
        if temp2:
            l1, l2 = l2, l1
        temp = temp1 if temp1 else temp2
        rslt = None

        while temp:
            rslt = ListNode(l1.val, rslt)
            l1 = l1.next
            temp = temp.next
        while l1:
            rslt = ListNode(l1.val + l2.val, rslt)
            l1 = l1.next
            l2 = l2.next

        carry, prev = 0, None

        while rslt:
            tempv = rslt.val + carry
            carry, tempv = tempv//10, tempv%10
            rslt.val = tempv
            temp = rslt.next
            rslt.next = prev
            prev = rslt
            rslt = temp

        if carry:
            prev = ListNode(carry, prev)
        return prev
