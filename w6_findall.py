import re
while True:
    line = input()
    if line == "":
        break
    parsed_line = re.findall("<i>(.*?)</i>", line)
    if len(parsed_line) != 0:
        print(*re.findall("<i>(.*?)</i>", line), sep="\n")
