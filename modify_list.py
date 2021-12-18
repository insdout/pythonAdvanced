def modify_list(a):
    i = 0
    while i < len(a):
        if a[i] % 2 != 0:
            a.pop(i)
        else:
            a[i] = a[i] // 2
            i += 1
