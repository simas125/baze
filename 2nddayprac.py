# def count_digits(x):
#     if x <  10:
#         return 1
#     return 1 + count_digits(x//10)
# def sum_digits(x):
#     if x ==0:
#         return 0
#     return x%10 + sum_digits(x//10)
# def twoSum(nums, target):
#     seen = set()
#     for i in nums:
#         reikia = target - i
#         if reikia in seen:
#             return(reikia, i)
#         seen.add(i)
def first(zodis):
    seen = {}
    for raide in zodis:
        if raide not in seen:
            seen[raide] = 1
        seen[raide] += 1
    for j in zodis:
        if seen[j] == 1:
            return j
