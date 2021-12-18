N = int(input())
possible_numbers = set(range(1, N+1))
ans = []
while True:
    line = input()
    if line == "HELP":
        break
    else:
        temp = set([int(x) for x in line.split()])
        if len(temp.intersection(possible_numbers)) <= \
                len(possible_numbers.difference(temp)):
            ans.append("NO")
            possible_numbers.difference_update(temp)
        else:
            ans.append("YES")
            possible_numbers.intersection_update(temp)
print(*ans, sep='\n')
print(*sorted(possible_numbers))
