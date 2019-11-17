def top_n_competitors(competitors, reviews, k):
    if not competitors or not reviews:
        return []
    
    # Get counts of competitors in reviews
    counts = {competitor: 0 for competitor in competitors}
    for review in reviews:
        for word in review.split():
            word = word.lower()
            if word in counts:
                counts[word] += 1
    
    # Sort by the count first
    counts = sorted(counts.items(), key = lambda x: x[0])

    # Sort by lexicographical order
    return [word for word, count in sorted(counts, key = lambda x: x[1], reverse = True)][:k]
