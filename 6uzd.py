def hasPair(nums, target):
    seen = {}
    for i in range(len(nums)):
        reikia = target - nums[i]
        if reikia in seen:
            return(True)
        seen[nums[i]]= i
    return False