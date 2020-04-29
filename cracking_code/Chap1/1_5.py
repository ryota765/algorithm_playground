s1 = input()
s2 = input()


# O(N)
def func(s1,s2):
    # 文字の置き換え
    if len(s1) == len(s2):
        count = 0
        for i,letter in enumerate(s1):
            if letter != s2[i]:
                count += 1
                if count >= 2:
                    return False
        return True
    # 文字の挿入・削除
    elif len(s1) - len(s2) == 1:
        count = 0
        s2_idx = 0
        for l in s1:
            if l == s2[s2_idx]:
                s2_idx += 1
                if s2_idx == len(s2):
                    return True
            else:
                count += 1
                if count >= 2:
                    return False
        return True
    elif len(s2) - len(s1) == 1:
        count = 0
        s1_idx = 0
        for l in s2:
            if l == s1[s1_idx]:
                s1_idx += 1
                if s1_idx == len(s1):
                    return True
            else:
                count += 1
                if count >= 2:
                    return False
        return True
    return False
    

print(func(s1,s2))