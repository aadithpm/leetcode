
def rearrange(elements):
    counts = {}
    for i in range(len(elements)):
        count = 0
        num = elements[i]
        while num:
            if num & 1:
                count += 1
            num = num >> 1
        if count in counts:
            counts[count].append(elements[i])
        else:
            counts[count] = [elements[i]]
    res = []
    for count in sorted(counts.keys()):
        res.extend(sorted(counts[count]))
    return res

