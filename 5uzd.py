def twoSum(nums,target):
    a = {}
    for i, num in enumerate(nums):
        reikia = target - num
        if reikia in a:
            return[a[reikia], i]
        a[num]=i