import json
d0 = []
files = input().split()
output_file = input()
for file in files:
    with open(file) as f0:
        for ln in f0:
            d0.append(json.loads(ln))

out_put = map(
    lambda x: x['date'] + "\t" + x['message'] + "\n",
    sorted(
        d0, key=lambda x: (x['date'], x['consumer_id'])
    )
)

with open(output_file, mode="w") as f0:
    f0.write("".join(j for j in out_put))
