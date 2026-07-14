from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = Counter(s)
        t_count = Counter(t)

        for c in s:
            if s_count[c] != t_count[c]:
                return False
        
        return True