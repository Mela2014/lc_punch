class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
            if (left+right)//2 == mid:
                left += 1
        return right
