sales = {}
while True:
    input_line = input()
    if input_line == "":
        break
    name, item, qt = input_line.split()
    sales[name] = sales.get(name, dict())
    sales[name][item] = sales[name].get(item, 0) + int(qt)
for name in sorted(sales):
    print(name, ":", sep="")
    for item in sorted(sales[name]):
        print(item, sales[name][item])
