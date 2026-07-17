class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == need:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            # add the new character entering the window
            window[s2[right]] += 1

            # remove the character leaving the window (leftmost)
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]  # keep Counter clean for accurate == comparison
            left += 1

            if window == need:
                return True

        return False