N = int(input())
stress_dict = {}
error = 0
for i in range(N):
    word = input()
    if word not in stress_dict:
        stress_dict[word] = word
homework = input().split()
dict_keys_set = set([x.lower() for x in stress_dict.keys()])
for word in homework:
    if word in stress_dict:
        pass
    elif word.lower() in dict_keys_set:
        error += 1
    elif sum([1 for x in word if x == x.upper()]) != 1:
        error += 1
    else:
        pass
print(error)
