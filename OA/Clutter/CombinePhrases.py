def generate_phrases(phrases):

    first = {}
    last = {}
    combined = []

    for idx, phrase in enumerate(phrases):
        words = phrase.split()
        f, l = words[0], words[len(words) - 1]
        if f in first:
            first[f].append(' '.join(phrase.split()[1:]))
        else:
            first[f] = [' '.join(phrase.split()[1:])]
       
        if l in last:
            last[l].append(phrase)
        else:
            last[l] = [phrase]

    for word in last:
        if word in first:
            for fcombo in first[word]:
                for lcombo in last[word]:
                    combined.append(lcombo + ' ' + fcombo)

    return combined
