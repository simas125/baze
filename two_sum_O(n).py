def twosum(nums, target):
    seen = set()
    for num in nums:
        reikia = target - num
        if reikia in seen:
            return(True)
        else:
            seen.add(num)
    return(False)