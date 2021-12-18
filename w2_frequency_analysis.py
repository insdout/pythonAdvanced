text_dict = {}
while True:
    input_line = input()
    if input_line == "":
        break
    for word in input_line.split():
        text_dict[word] = text_dict.get(word, 0) + 1
print(*sorted(text_dict, key=lambda x: (-text_dict[x], x),
              reverse=False), sep="\n")
