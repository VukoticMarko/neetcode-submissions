class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            incoming[dst] += 1 # People that trust certain amount of people
            outgoing[src] += 1 # Does a certain person trust someone? 0 if he/she doesn't

        for i in range(1, n + 1):
            # Judge is trusted by everyone except by himself n-1 and trusts no one 0
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i

        return -1