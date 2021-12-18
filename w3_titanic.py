import numpy as np
data = []
with open("titanic.csv") as f:
    for line in f:
        data.append(line.rstrip().replace(', '," ").split(","))

data_np = np.array(data[1::]).transpose()
print(data_np)
print(*enumerate(data[0]))
print("Entries: ", len(data_np[0]))
print("Males: ", sum([1 if x == "male" else 0 for x in data_np[4]]))
print("Parch>0: ", sum([1 if int(x) > 0 else 0 for x in data_np[7]]))
print("First Class: ", round(sum([1 if x == "1" else 0 for x in data_np[2]])/len(data_np[0]), 2))
print("Sur/all: ", round(sum([1 if x == "1" else 0 for x in data_np[1]])/len(data_np[0]), 2))
print("Sur/FC: ", round(sum([1 if str(data_np[1][i]) == "1" and str(data_np[2][i]) == "1" else 0 for i in range(len(data_np[1]))])/sum([1 if x == "1" else 0 for x in data_np[2]]), 2))
print("Mean age", round(sum([int(x) for x in data_np[5] if x.isdigit()])/sum([1 for x in data_np[5] if x.isdigit()]), 2))
print("Median age", round(np.median([int(x) for x in data_np[5] if x.isdigit()]), 2))
ages = {}
for x in data_np[5]:
    ages.setdefault(x,0)
    ages[x] += 1
print("Most Common Age: ", sorted(ages, key=lambda x: ages[x], reverse=True)[1])
age = []
for x in  data_np[5]:
    if x != "":
        age.append(float(x))

print("Mean Age: ", np.mean(age))