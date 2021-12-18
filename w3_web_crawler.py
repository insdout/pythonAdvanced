import json
file_name = input()


def parse_dict(d, catalog=[], path=""):
    if len(d.keys()) == 0:
        catalog.append(path[:-1])
        return catalog
    else:
        for key in d.keys():
            temp = str(path)
            path += key + "/"
            parse_dict(d[key], catalog, path)
            path = temp
    return catalog


with open(file_name) as f:
    for line in f:
        ln = json.loads(line)
        result = parse_dict(ln)
        print(*sorted(result), sep="\n")
