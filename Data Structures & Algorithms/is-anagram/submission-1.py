from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sC = Counter(s)
        tC = Counter(t)

        for c in s:
            if sC[c] != tC[c]:
                return False
        return True