def first_nr(s):
    seen = {}
    for i in range(len(s)):
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    return seen
    for i in seen:
        if seen[i] == 1:
            print(i)
            break
        else:
            print(None)