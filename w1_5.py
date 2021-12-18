N, K = [int(x) for x in input().split()]
weekends = set(range(6, N+1, 7))
weekends.update(set(range(7, N+1, 7)))
strikes = set()
for i in range(K):
    a, b = [int(x) for x in input().split()]
    strikes.update(range(a, N+1, b))
strikes.difference_update(weekends)
print(len(strikes))
