def twoSum(nums, target):
    a = {}
    for i in range(len(nums)):
        reikia = target - nums[i]
        if reikia in a:
            return[a[reikia], i]
        a[nums[i]] = i
