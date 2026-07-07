class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # If I create a dictionary list, which holds the letter to an index,
        # And if I compare that list made for each word with every other word,
        # You can see which words in the list have the same characters,
        # And then I can add them to a list.
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                val = ord(c) - ord('a')
                count[val] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())