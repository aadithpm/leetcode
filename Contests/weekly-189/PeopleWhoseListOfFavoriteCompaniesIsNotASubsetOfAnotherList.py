class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        buckets = {}
        res = []
        for favorite in favoriteCompanies:
            if len(favorite) in buckets:
                buckets[len(favorite)].append(set(favorite))
            else:
                buckets[len(favorite)] = [set(favorite)]
        
        for idx, favorite in enumerate(favoriteCompanies):
            length = len(favorite)
            found = False
            for key, companies in buckets.items():
                if key > length:
                    for company in companies:
                        if set(favorite).issubset(company):
                            found = True
                            break
            if not found:
                res.append(idx)
        
        return res
