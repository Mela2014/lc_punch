class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        dque, seen1, seen2, rslt, limit = collections.deque([(0, 1)]), set(forbidden), set(forbidden), 0, max(x, max(forbidden)) + a + b
        while dque:
            for _ in range(len(dque)):
                cur, last_forward = dque.popleft()
                if cur == x:
                    return rslt
                if cur + a <= limit and cur + a not in seen1:
                    seen1.add(cur + a)
                    dque.append((cur + a, 1))
                if cur - b > 0 and cur - b not in seen2 and last_forward:
                    seen2.add(cur - b)
                    dque.append((cur - b, 0))
            rslt += 1
        return -1
