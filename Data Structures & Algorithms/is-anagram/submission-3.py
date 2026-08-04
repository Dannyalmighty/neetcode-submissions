from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCounter = Counter(s)
        tCounter = Counter(t)

        for c in s:
            if sCounter[c] != tCounter[c]:
                return False
        
        return True