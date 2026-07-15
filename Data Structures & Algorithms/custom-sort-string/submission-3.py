class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create frequency count of s, mapping letter to amount
        mp = [0] * 26
        ans = []
        for i in s:
            val = (ord(i) - ord('a'))
            mp[val] += 1
        # Find index value of each char in freq count, iterate through order
        # Subtract char value from mp if still in freq count, add to potential answer
        for x in order:
            idx = ord(x) - ord('a')
            while mp[idx]:
                mp[idx] -= 1
                ans.append(x)

        # Loop through each index of characters, if theres anything left
        # in freq count, subtract it, add it to end of list
        for idx in range(26):
            c = chr(idx + ord('a'))
            while mp[idx]:
                mp[idx] -= 1
                ans.append(c)

        #return    result word
        return "".join(ans)