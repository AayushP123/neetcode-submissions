class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for v, n in enumerate(t):
                if n == target[v]:
                    ans.add(v)
        return len(ans) == 3