class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # inorder traversal
        def inorder(root):
            if not root:
                return None, None
            left, right = root.left, root.right
            head, tail = inorder(left)
            if head:
                tail.right = root
                root.left = tail
            else:
                head = root
            nhead, ntail = inorder(right)
            root.right = nhead
            if nhead:
                nhead.left = root
            else:
                ntail = root
            return head, ntail
        head, tail = inorder(root)
        if not head: return None
        head.left = tail
        tail.right = head
        return head
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        dummy = Node(0)
        prev = dummy
        stack, curr = [], root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr.left = prev
            prev.right = curr
            prev = curr
            curr = curr.right
        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right
