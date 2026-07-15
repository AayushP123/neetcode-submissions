class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        mp = defaultdict(list)
        # Map username to timestamp and website
        for u, t, w in zip(username, timestamp, website):
            mp[u].append((t, w))
        
        # Sort by time stamp because its first in the list
        for u in mp:
            mp[u].sort()
        
        # Create dictionary holding the amount of each set.
        # All you need is the timestamp and website for each u, put that into a variable
        # Create all the sequences in a set 
        count = defaultdict(int)
        for u in mp:
            possibleSets = [w for t, w in mp[u]]
            sequences = set(combinations(possibleSets, 3))
            for seq in sequences:
                count[seq] += 1
        
        maxCount = max(count.values())
        best_seq = min(seq for seq, c in count.items() if c == maxCount)
        return list(best_seq)