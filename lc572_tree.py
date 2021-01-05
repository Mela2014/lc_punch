class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSametree(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return s.val == t.val and isSametree(s.left, t.left) and isSametree(s.right, t.right)
        if not t: return True
        return s and (isSametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
