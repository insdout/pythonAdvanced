text = []
word_pos = {}
ans = []
while True:
    line = input()
    if line == "":
        break
    text.extend(line.split())
for i in range(len(text)):
    if text[i] in word_pos:
        ans.append(word_pos[text[i]])
        word_pos[text[i]] = i
    else:
        word_pos[text[i]] = i
        ans.append(-1)
print(*ans, sep=" ")
