class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for i in s:
                chars[ord(i) - ord('a')] += 1
            ans[tuple(chars)].append(s)
        return list(ans.values())