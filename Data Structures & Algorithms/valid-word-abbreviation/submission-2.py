class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Create pointer for word and abbr, move each, compare
        # If they are the same LETTER, continue until there is a
        # difference. If it is a letter diff, return false, if it is
        # a number diff, loop until it is NOT a number
        # Find how much to move word pointer by, add to word.
        n = len(word)
        k = len(abbr)
        i = 0
        j = 0

        while i < n and j < k:
            if abbr[j] == '0':
                return False
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha():
                return False
            else:
                val = 0
                while j < k and abbr[j].isdigit():
                    val = val * 10 + int(abbr[j])
                    j += 1
                i += val
        return i == n and j == k