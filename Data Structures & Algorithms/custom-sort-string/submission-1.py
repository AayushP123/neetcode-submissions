class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freqCount = [0] * 26 # map char to amount
        ans = []
        for i in s:
            freqCount[(ord(i) - ord('a'))] += 1
        
        # for each letter in order, subtract one from freq map when encountered, append to ans.
        for x in order:
            idx = ord(x) - ord('a')
            while freqCount[idx] > 0:
                freqCount[idx] -= 1
                ans.append(x)
        
        # for remaining letters in s, not in order, loop through s,
        # while count > 0, append to end of list.
        for y in s:
            idx = ord(y) - ord('a')
            while freqCount[idx] > 0:
                freqCount[idx] -= 1
                ans.append(y)

        return ''.join(ans)