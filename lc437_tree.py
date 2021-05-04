class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node, curr):
            if not node:
                return
            curr += node.val
            if curr == sum:
                self.count += 1
            self.count += maps[curr-sum]
            maps[curr] += 1
            preorder(node.left, curr)
            preorder(node.right, curr)
            maps[curr] -= 1
        self.count, maps = 0, collections.defaultdict(int)
        preorder(root, 0)
        return self.count
