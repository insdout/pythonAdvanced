N = int(input())
num_dict = {}
for _ in range(N):
    num = int(input())
    val = sum([int(str(num)[i]) - int(str(num)[-i-1])
               for i in range(len(str(num))//2)])
    num_dict.update({num: val})
print(num_dict)
print(*sorted(num_dict, key=lambda x: (num_dict[x], x)), sep="\n")


def f(digit):
    s = 0
    for i in range(len(digit) // 2):
        a = int(digit[i])
        b = int(digit[-(i + 1)])
        s += (a - b)
    return s, int(digit)
digits = [str(x) for x in num_dict.keys()]
for key in digits:
    print(f(key))

print(*sorted(digits, key=f), sep='\n')