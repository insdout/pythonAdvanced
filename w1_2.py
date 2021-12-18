N = int(input())
possible_numbers = set(range(1, N+1))

temp = set()
while True:
    line = input()
    if line == "HELP":
        break
    elif line == "YES":
        possible_numbers.intersection_update(temp)

    elif line == "NO":
        possible_numbers.difference_update(temp)

    else:
        temp = set([int(x) for x in line.split()])

print(*sorted(possible_numbers))
