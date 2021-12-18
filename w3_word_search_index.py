import json
N = int(input())
words = [input() for _ in range(N)]
dic_w = {}
output_file = input()
keys = set([word[0] for word in words])
for key in keys:
    dic_w.setdefault(key, {})
    for key_2 in set(
            [word[:2] for word in words if word[0] == key]
    ):
        dic_w[key].setdefault(key_2, {})
        dic_w[key].update({key_2: sorted(
            [word for word in words if word[:2] == key_2]
        )})

with open(output_file, mode="w") as f:
    json.dump(dic_w, f)
