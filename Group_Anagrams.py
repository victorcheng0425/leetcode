##dictionary, similar to hash function
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for x in strs:
            key = tuple(sorted(x))
            if key in res:
                res[key].append(x)
            else:
                res[key] = [x]
        return res.values()
