import json

input_files = input().split()
output_file = input()

data = []
print(input_files[0], input_files[1])
print(input_files)
for file in input_files:
    with open(file) as f_0:
        for i in f_0:
            data.append(json.loads(i))

data.sort(key=lambda x: (x["date"], x["consumer_id"]))

with open(output_file, "w") as f_2:
    for i in data:
        f_2.write(i["date"] + "\t" + i["message"] + "\n")
