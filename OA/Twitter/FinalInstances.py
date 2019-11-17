def finalInstances(instances, averageUtil):
   
    i, n, res = 0, len(averageUtil), instances

    while i < n:
        if averageUtil[i] < 25 and res > 1:
            res, i = (res + 1) // 2, i + 10
        elif averageUtil[i] > 60 and res <= int(1e8):
            res, i = res * 2, i + 10
        i += 1
   
    return res
