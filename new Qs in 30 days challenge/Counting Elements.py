from collections import defaultdict, Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        # s = set()
        if not arr:
            return 0
        
        c_map = Counter(arr)
        keys, counts = list(c_map.keys()), list(c_map.values())
        res = 0
        for i, k in enumerate(keys):
            if k+1 in keys:
                res += counts[i]

        return res