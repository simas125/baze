def first_unique(s):
    seen = {}
    for i in s:
        if i in seen:
            seen[i] += 1
        elif i not in seen:
           seen[i] = 1
    for i in s:
        if seen[i] == 1:
            return i
        
    return None