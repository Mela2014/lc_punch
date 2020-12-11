class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        dqueue = collections.deque([root])
        rslt = []
        while dqueue:
            temp = dqueue.popleft()
            if temp:
                rslt.append(str(temp.val))
                dqueue.append(temp.left)
                dqueue.append(temp.right)
            else:
                rslt.append("")
        return ",".join(rslt)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dqueue = collections.deque([])
        root, check = None, 0
        for val in data.split(","):
            temp = TreeNode(int(val)) if val != "" else None
            if not root:
                root = temp
                dqueue.append(root)
            else:
                if check == 0:
                    dqueue[0].left = temp
                    check += 1
                else:
                    dqueue[0].right = temp
                    dqueue.popleft()
                    check = 0
                if temp: dqueue.append(temp)
        return root
