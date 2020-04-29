s = input()
s = s.replace(' ','')

# O(N)
def func(s):
    hash_list = [0 for i in range(128)]
    for l in s:
        if hash_list[ord(l)] == 0:
            hash_list[ord(l)] += 1
        else:
            hash_list[ord(l)] -= 1
    if sum(hash_list) <= 1:
        return True
    else:
        return False

print(func(s))