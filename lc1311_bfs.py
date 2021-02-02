class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited, dque = {id}, collections.deque([id])
        while dque:
            if level == 0:
                break
            size = len(dque)
            for _ in range(size):
                curr = dque.popleft()
                for nt in friends[curr]:
                    if nt not in visited:
                        visited.add(nt)
                        dque.append(nt)
            level -= 1
        rslt = []
        while dque:
            rslt.extend(watchedVideos[dque.pop()])
        summary = collections.Counter(rslt)
        return sorted(summary.keys(), key = lambda x: (summary[x], x))
