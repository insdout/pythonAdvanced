word_count = {}
while True:
    line = input()
    if line == "":
        break
    else:
        for word in line.split():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
max_val = max(word_count.values())
res = [k for k, v in word_count.items() if v == max_val]
print(sorted(res)[0])
