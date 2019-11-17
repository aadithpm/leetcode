def countGroups(related):
    related = [[int(j) for j in i] for i in related]
    seen = set()
    groups = 0

    def dfs(pos):
        for idx, follower in enumerate(related[pos]):
            if follower and idx not in seen:
                seen.add(idx)
                dfs(idx)

    for i in range(len(related)):
        if i not in seen:
            dfs(i)
            groups += 1
   
    return groups
