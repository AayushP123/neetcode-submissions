class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            char = [0] * 26
            for n in s:
                char[ord(n) - ord('a')] += 1
            ans[tuple(char)].append(s)
        return list(ans.values())