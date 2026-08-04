class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortWord = ''.join(sorted(s))
            res[sortWord].append(s)
        
        return list(res.values())