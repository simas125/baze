def twosum(nums, target):
    seen = {}
    for i in range(len(nums)):
        reikia = target - nums[i]
        if reikia in seen:
            return[seen[reikia], i]
        seen[nums[i]]=i
nums = [2, 7, 11, 15]
target = 9
rezultatas = twosum(nums, target)
print(rezultatas)