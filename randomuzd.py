# # masyvo suma be sum()
# a = [1, 2, 3, 4]
# suma = 0
# for i in a:
#     suma += i
# print(suma)
#didziausias be max
# a = [5, 1, 9, 3]
# didz=a[0]
# for i in a:
#     if i>didz:
#         didz=i
# print(didz)
## surast lyginius 
# a = [1, 2, 3, 4, 6]
# lyg = 0
# for i in a:
#     if i%2 == 0:
#         lyg += 1
# print(lyg)
## surast antra didziausia
# a = [5, 1, 9, 3, 8]
# didz= a[0]
# antr = float('-inf')
# for i in rangzodis = "banana"
# raides = {}
# for i in zodis:
#     if i not in raides:
#         raides[i] = 1
#     elif i in raides:
#         raides[i] = raides[i] + 1
# print(raides)e(len(a)):
#     if a[i] > didz:
#         antr = didz
#         didz = a[i]
#     elif didz > a[i] > antr:
#         antr = a[i]
# print(antr)
## string, dict, kiek raidziu ir po kiek kartu pasikartoja
# zodis = "banana"
# raides = {}
# for i in zodis:
#     if i not in raides:
#         raides[i] = 1
#     elif i in raides:
#         raides[i] = raides[i] + 1
# print(raides)
#
#
# def count_a(s):
#     sk = 0
#     for i in s:
#         if i == "a":
#             sk += 1
#     return sk
# s = "banana"
# sk = 0
# for i in s:
#     if i == "a":
#         sk += 1
# print(sk)
# lst = [1, 5, 8, 2, 8]
# if 5 in lst:
#     print("yes")
# else:
#     print("no")
# n = -3
# if n > 0:
#     print("positive")
# else:
#     print("not positive")
# lst = [4, 7, 1, 9]
# didz = lst[0]
# for i in lst:
#     if i > didz:
#         didz = i
# print(didz)
# lst = [5, 5, 3]
# didz = lst[0]
# antr = float("-inf")
# for i in lst:
#     if i > didz:
#         antr = didz
#         didz = i
#     elif didz > i > antr:
#         antr = i
# print(antr, didz)
s = "mississippi"
seen = {}
for i in s:
    if i in seen:
        seen[i] += 1
    else:
        seen[i] = 1
print(seen)