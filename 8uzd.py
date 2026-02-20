def first_nr(s):
    seen = {}
    for i in s:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    for i in s:
        if seen[i] == 1:
            return(i)
    return None