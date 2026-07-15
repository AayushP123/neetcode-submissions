class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Create dictionary holding list
        ans = defaultdict(list)

        # At some point, will need to map name to timestamp and word in freq count
        for u, t, w in zip(username, timestamp, website):
            ans[u].append((t, w))

        # Sort list by timestamp
        for u in ans:
            ans[u].sort()

        # Basically check which score is largest from list, add to new dict
        # Make sure to set one user max to 1, 3 diff possible combinations.
        count = defaultdict(int)
        for u in ans:
            possibleSets = [w for t, w in ans[u]]
            sequences = set(combinations(possibleSets, 3))
            for seq in sequences:
                count[seq] += 1

        # Return list by finding the max, or sorting lexicographically
        res = max(count.values())
        best_seq = min(seq for seq, c in count.items() if c == res)
        return list(best_seq)