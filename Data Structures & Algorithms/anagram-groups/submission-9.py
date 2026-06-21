class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        smallAns = {} # Map char to val

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in ans:
                ans[key] = []
            ans[key].append(word)
        return list(ans.values())