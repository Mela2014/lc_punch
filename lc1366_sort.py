class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        l = len(votes[0])
        mapping = {k: [0]*l for k in votes[0]}
        for vote in votes:
            for i, v in enumerate(vote):
                mapping[v][i] += 1
        return "".join(sorted(mapping.keys(), key = lambda x: (-mapping[x], x)))
