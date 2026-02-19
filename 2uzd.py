def countletters(s):
    b = {}
    for letter in s:
        b[letter] = b.get(letter, 0) + 1
    return b
print(countletters("abasfkmkamls;mfhdkhmfdsok asfaskgmako asgfam"))