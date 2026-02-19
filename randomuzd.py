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
# for i in range(len(a)):
#     if a[i] > didz:
#         antr = didz
#         didz = a[i]
#     elif didz > a[i] > antr:
#         antr = a[i]
# print(antr)
zodis = "banana"
raides = {}
for i in zodis:
    if i not in raides:
        raides[i] = 1
    elif i in raides:
        raides[i] = raides[i] + 1
print(raides)