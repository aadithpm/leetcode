def waitingTime(tickets, p):
    total = tickets[p]
    for idx, person in enumerate(tickets):
        if idx != p:
            if person < tickets[p]:
                total += person
            else:
                total += tickets[p]
                if idx > p:
                    total -= 1
    return total
