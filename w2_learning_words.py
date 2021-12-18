N = int(input())
w_dict = {}
for _ in range(N):
    word = input()
    w_dict.update({word: len(word)})
print(*sorted(w_dict, key=lambda x: (w_dict[x], x[::-1])), sep="\n")
