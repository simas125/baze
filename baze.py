# 1 for i in range(10, 0, -1):
#    print(i)**
# 2 for i in range(2, 21, 2):
#     print(i)
# 3 a = int(input("tavo n: "))
# suma=0
# for i in range(1, a + 1):
#     suma+=i
# print(suma)
# 4 a = [3, 7, 2, 9, 5, 99]
# did = a[0]
# for elementas in a:
#     if elementas > did:
#         did = elementas
# print(did)
# 5 a = [1, 2, 3, -1, -2, 0, 5, -5]
# suma = 0
# for i in a:
#     if i>0:
#         suma = suma + 1
# print(suma)
# 6 b = ("radar", "anna", "python", "12321")
# for zodis in b:
#     if zodis == zodis[::-1]:
#         print(zodis)
# 7 didz = 0
# antras = 0
# sar = [2, 1, 3, 2, 5, 6, 4, 8, 7, 9, 15, 12, 11, 14, 10]
# for i in sar:
#     if i>didz:
#         antras=didz
#         didz=i
#     elif didz>i>antras:
#         antras=i
# print(didz)
# print(antras)
# 8 nums = [2, 7, 11, 15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
# seen = {}
# 9 target = 9
# nums = [2, 7, 11, 15]
# for i in range(len(nums)):
#     reikia = target - nums[i]
#     if reikia in seen:
#         print("Sprendimas yra ", reikia, nums[i])
#     else:
#         seen[nums[i]] = i
tikr = {}
ok = True
a = input(str("Pirmas zodis: "))
b = input(str("Antras zodis: "))
for raide in a:
    if raide in tikr:
        tikr[raide] = tikr[raide] + 1
    else:
        tikr[raide] = 1

for raide in b:
    if raide in tikr:
        tikr[raide] = tikr[raide] - 1
    else:
        ok = False
        break
for kiekis in tikr.values():
    if kiekis != 0:
        ok = False
        break
if ok:
    print("Anagrama")
else:
    print("ne anagrama")