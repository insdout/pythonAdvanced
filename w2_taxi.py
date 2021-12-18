km = sorted([int(x) for x in input().split()])
price = sorted([int(x) for x in input().split()], reverse=True)
print(sum([km[i] * price[i] for i in range(len(km))]))
