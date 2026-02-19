def twoSum(nums, target):
    sum = 0
    sk = 0
    for i in range(nums):
        sum = sk[i] + sk[i+1]
        if sum == target:
            return sk[i] and sk[i+1]
    
