size = int(input())
shoes = sorted([int(x) for x in input().split()])
pairs = 0
min_val = 0
for i in range(len(shoes)):
    if min_val == 0:
        if shoes[i] >= size:
            min_val = shoes[i]
            pairs += 1
    else:
        if shoes[i]-min_val >= 3:
            min_val = shoes[i]
            pairs += 1

customer_size = size
sizes = shoes
sorted_sized = sorted(sizes)

list_remain = []
for i in sorted_sized:
    if i >= customer_size:
        list_remain.append(i)
    else:
        print(0)
if len(list_remain) > 0:
    list_count = [list_remain[0]]

    for j in range(0, len(list_remain)-1):
        if list_remain[j+1] - list_count[-1] >= 3:
            list_count.append(list_remain[j+1])
    print("Your:",len(list_count))


print("Mine:", pairs)
