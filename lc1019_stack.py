# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# maintain a monotonic decreasing stack
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        answer, stack, i = [], [], 0
        while head:
            while stack and stack[-1][0] < head.val:
                _, j = stack.pop()
                answer[j] = head.val
            stack.append((head.val, i))
            answer.append(0)
            head = head.next
            i = i+1
        return answer
