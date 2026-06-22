class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            signature = tuple(sorted(word))
            if signature not in groups:
                groups[signature] = [word]
            else:
                groups[signature].append(word)
         
        return list(groups.values())