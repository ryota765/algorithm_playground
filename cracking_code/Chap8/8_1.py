n = int(input())

used_dict = {}

def count_step(n):
    if n == 3:
        return 4
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        if str(n-1) in used_dict:
            elem1 = used_dict[str(n-1)]
        else:
            used_dict[str(n-1)] = count_step(n-1)
            elem1 = used_dict[str(n-1)]
        if str(n-2) in used_dict:
            elem2 = used_dict[str(n-2)]
        else:
            used_dict[str(n-2)] = count_step(n-2)
            elem2 = used_dict[str(n-2)]
        if str(n-3) in used_dict:
            elem3 = used_dict[str(n-3)]
        else:
            used_dict[str(n-3)] = count_step(n-3)
            elem3 = used_dict[str(n-3)]

        return elem1+elem2+elem3

print(count_step(n),used_dict)