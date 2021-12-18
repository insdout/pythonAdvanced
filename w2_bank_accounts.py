bank_accounts = {}
ans = []
while True:
    line = input()
    if line == "":
        break
    line_split = line.split()
    if line_split[0] == "DEPOSIT":
        name = line_split[1]
        amount = int(line_split[2])
        if name not in bank_accounts:
            bank_accounts[name] = 0
        bank_accounts[name] += amount
    elif line_split[0] == "WITHDRAW":
        name = line_split[1]
        amount = int(line_split[2])
        if name not in bank_accounts:
            bank_accounts[name] = 0
        bank_accounts[name] -= amount
    elif line_split[0] == "BALANCE":
        name = line_split[1]
        if name not in bank_accounts:
            ans.append("ERROR")
            continue
        ans.append(bank_accounts[name])
    elif line_split[0] == "TRANSFER":
        name_from = line_split[1]
        name_to = line_split[2]
        amount = int(line_split[3])
        if name_from not in bank_accounts:
            bank_accounts[name_from] = 0
        if name_to not in bank_accounts:
            bank_accounts[name_to] = 0
        bank_accounts[name_to] += amount
        bank_accounts[name_from] -= amount
    elif line_split[0] == "INCOME":
        value = float(line_split[1])
        for name in bank_accounts:
            if bank_accounts[name] > 0:
                bank_accounts[name] = int(round(bank_accounts[name]
                                                + bank_accounts[name]
                                                * value / 100, 7))
print(*ans, sep="\n")
