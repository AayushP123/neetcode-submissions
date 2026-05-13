class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for x in s:
                count[ord(x) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
