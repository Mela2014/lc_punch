class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, rslt, count , count_dict= 0, 0, 0, collections.defaultdict(int)
        for right, c in enumerate(s):
            if count_dict[c] == 0:
                count += 1
            count_dict[c] += 1
            while count == 3:
                count_dict[s[left]] -= 1
                if count_dict[s[left]] == 0:
                    count -= 1
                left += 1
                rslt += len(s) - right
        return rslt
