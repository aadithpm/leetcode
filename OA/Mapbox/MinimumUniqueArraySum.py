def getMinimumUniqueSum(arr):
    numbers = set()
    indices = set()
    for idx, num in enumerate(arr):
        if num not in arr:
            numbers.add(num)
        else:
            indices.add(idx)
    for idx in indices:
        while arr[idx] in numbers:
            arr[idx] += 1
        numbers.add(arr[idx])
    return sum(numbers)
