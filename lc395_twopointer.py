#divide and conquer
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = collections.Counter(s)
        for t in counts:
            if counts[t] < k:
                return max(self.longestSubstring(ss, k) for ss in s.split(t))
        return len(s)

#sliding window
class Solution:
    def longestSubstring(self, s, k):
        count = 0
        for i in range(1, 27):
            count = max(count, self.helper(s, k, i))
        return count

    def helper(self, s, k, numUniqueTarget):
        start = end = numUnique = numNoLessThanK = count = 0
        chMap = [0]*128

        while end < len(s):
            if chMap[ord(s[end])] == 0: numUnique += 1
            chMap[ord(s[end])] += 1
            if chMap[ord(s[end])] == k: numNoLessThanK += 1
            end += 1

            while numUnique > numUniqueTarget:
                if chMap[ord(s[start])] == k: numNoLessThanK -= 1
                chMap[ord(s[start])] -= 1
                if chMap[ord(s[start])] == 0: numUnique -= 1
                start += 1

            if numUnique == numNoLessThanK: count = max(count, end-start)

        return count
