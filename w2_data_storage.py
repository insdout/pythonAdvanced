disk_space, users = [int(x) for x in input().split()]
backups = []
ans = 0
for i in range(users):
    backups.append(int(input()))
backups.sort()
for i in range(1, len(backups)+1):
    if disk_space == 0:
        break
    if sum(backups[:i]) <= disk_space:
        ans = i
    else:
        break
print(ans)
