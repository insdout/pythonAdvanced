votes = {}
while True:
    line = input()
    if line == "VOTES:":
        break
    if line == "PARTIES:":
        continue
    votes[line] = 0
while True:
    line = input()
    if line == "":
        break
    votes[line] += 1
total_votes = sum(votes.values())
ans = [x for x in votes if round(100 * votes[x] / total_votes, 4) >= 7]
print(*ans, sep="\n")
