class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += str(len(word)) + "#" + word
        return ans
    def decode(self, s: str) -> List[str]:
        l = 0
        ans = []

        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = length + l
            ans.append(s[l:r])
            l = r
        return ans