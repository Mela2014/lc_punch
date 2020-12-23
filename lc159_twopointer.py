class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        container, count, left, rslt = collections.defaultdict(int), 0, 0, 0
        for right, c in enumerate(s):
            if container[c] == 0:
                count += 1
            container[c] += 1
            while count > 2:
                container[s[left]] -= 1
                if container[s[left]] == 0:
                    count -= 1
                left += 1
            rslt = max(rslt, right-left+1)
        return rslt
