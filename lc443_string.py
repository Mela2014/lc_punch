class Solution:
    def compress(self, chars: List[str]) -> int:
        rslt, cnt, left = 0, 0, 0
        for i, ch in enumerate(chars+[")"]):
            if i > 0 and ch != chars[i-1]:
                chars[left] = chars[i-1]
                left += 1
                if cnt > 1:
                    for t in str(cnt):
                        chars[left] = t
                        left += 1
                    cnt = 1
            else:
                cnt += 1
        return left
