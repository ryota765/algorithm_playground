s = input()

'''
# O(N)?
def func(s):
    string_list = s.split()
    return '%20'.join(string_list)
    '''

# O(N)
def func(s):
    return s.replace(' ', '%20')

print(func(s))