def duplicate_or_unique(inList):
    count = {}
    for num in inList:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    for num, freq in count.items():
        if freq == 1:
            if len(count) == (len(inList) + 1) // 2:
                return num
            elif freq == 2:
            if len(count) == len(inList) - 1:
                return num