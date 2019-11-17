def strangeSort(mapping, nums):
    map_mapping = {}
    for idx, i in enumerate(mapping):
        map_mapping[str(i)] = idx

    this_mapping = {}
    for midx, num in enumerate(nums):
        this_num = 0
        l = len(num)
        for idx, i in enumerate(num):
            if i != 0:
                this_num += map_mapping[i] * (10 ** (l - idx))
        this_mapping[midx] = this_num
    
    return [nums[i[0]] for i in sorted(this_mapping.items(), key=lambda x: x[1])]
