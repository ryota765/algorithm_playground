s = input()

prev_str = ''
return_list = []
count = 0
stop_num = len(s) - 1

# 0(N)
for i,l in enumerate(s):
    if i == 0:
        prev_str = l
    elif l == prev_str:
        count += 1
        if i == stop_num:
            return_list.append(prev_str + str(count+1))
    else:
        return_list.append(prev_str + str(count+1))
        prev_str = l
        count = 0

if len(return_list) < len(s):
     print(''.join(return_list))
else:
    print(s)

