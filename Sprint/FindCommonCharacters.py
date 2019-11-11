from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counters = [Counter(i) for i in A]
        check = counters[0]
        for counter in counters[1:]:
            keys = list(check.keys())
            for key in keys:
                if key in counter:
                    check[key] = min(counter[key], check[key])
                else:
                    del check[key]
        
        return [i for k, v in check.items() for i in k * v]
