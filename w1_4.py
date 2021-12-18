N = int(input())
s_c = set()
for i in range(N):
    n_l = int(input())
    s = set()
    for j in range(n_l):
        s.add(input())
    if i == 0:
        s_c.update(s)
    else:
        s_c.intersection_update(s)
print(len(s_c))
print(*sorted(s_c), sep="\n")
