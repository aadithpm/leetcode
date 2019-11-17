def maxEvents(arrival, duration):
    events = sorted(zip(arrival, duration), key = lambda x: (sum(x), x[1]))
    possible = 0
    end_time = float('-inf')
    for event in events:
        if event[0] >= end_time:
            end_time = event[0] + event[1]
            possible += 1
    return possible
