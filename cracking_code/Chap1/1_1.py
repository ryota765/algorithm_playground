'''
# O(N^2)
def func(s):
    for l in s:
        if s.count(l) > 1:
            return 'False'
    return 'True'
    '''

'''
# O(NlogN)
def func(s):
    letters = [l for l in s]
    letters.sort()
    for i in range(len(s)-1):
        if letters[i] == letters[i+1]:
            return 'False'
    return 'True'
    '''

# O(N)
def func(s):
    letters = {}
    for l in s:
        if l in letters:
            return 'False'
        letters[l] = True
    return True

print(func(s = input()))

