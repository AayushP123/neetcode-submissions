class Solution:

    def encode(self, strs: List[str]) -> str:
        meow = ""
        for i in strs:
            meow += str(len(i)) + "#" + i
        return meow

    def decode(self, s: str) -> List[str]:
        meow = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            meow.append(s[i:j])
            i = j
            
        return meow