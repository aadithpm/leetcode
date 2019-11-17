def analyzeInvestments(s):
    """
    l = len(s)
    if l < 3:
        return 0

    count = 0
    companies = {"A", "B", "C"}
    s = list(s)
    
    for i in range(len(s) - 2):
        l, r = i, len(s) - 1
        while r > l:
            
            if all(i in s[l:r + 1] for i in companies):
                count += 1
            else:
                break
        
            r -= 1

    return count
    """
    hash = {'A' : [float('inf')], 'B' : [float('inf')], 'C' : [float('inf')] }
    for idx, letter  in enumerate(s):
        if letter in hash:
            hash[letter].append(idx)

    for i in hash:
        hash[i].sort()
    
    i = 0
    count = 0
    while i < len(s) - 2:
        a = hash['A'][0]
        if a == i :
            hash['A'].pop(0)
        b = hash['B'][0]
        if b == i :
            hash['B'].pop(0)
        c = hash['C'][0]
        if c == i :
            hash['C'].pop(0)

        k = max(a,b,c)
        if k == float('inf'):
            break
        count += len(s) - k
        i += 1
    return count
