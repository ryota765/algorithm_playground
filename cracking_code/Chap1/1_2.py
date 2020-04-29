s1 = input()
s2 = input()

'''
# O(NlogN)
def func(s1,s2):
    if len(s1) != len(s2):
        return False

    # O(NlogN)
    sort_1 = sorted([l for l in s1])
    sort_2 = sorted([l for l in s2])

    for i,elem in enumerate(sort_1):
        if sort_2[i] != elem:
            return False

    return True
    '''

# O(N)
def func(s1,s2):
    counts = [0 for i in range(128)] # ASCIIと仮定
    for l in s1:
        counts[ord(l)] += 1
    for l in s2:
        counts[ord(l)] -= 1
        if counts[ord(l)] < 0:
            return False
    if sum(counts) == 0:
        return True
    else:
        return False

print(func(s1,s2))