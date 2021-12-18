

def load_document(file_path):
    dic = {}
    with open(file_path, mode="r", encoding="utf-8") as f:
        for line in f:
            _id, rest = line.split(sep="\t", maxsplit=1)
            dic.update({int(_id): rest.strip()})
    return dic


def build_inverted_index(articles):
    rev_dict = {}
    for _key in articles:
        for val in set(articles[_key].split()):
            rev_dict.setdefault(val, set()).update({_key})
    return rev_dict


def build_inverted_index2(articles):
    new_dict = {}
    for key, value in articles.items():
        for item in value.split():
            new_dict.setdefault(item, []).append(key)

    new_dict2 = {k: set(v) for k, v in new_dict.items()}
    return new_dict2

file_path = "wikipedia_sample.txt"
dict = load_document(file_path)
bld1 = build_inverted_index(dict)
bld2 = build_inverted_index2(dict)
for key in bld2:
    if bld1[key] != bld2[key]:
        print(key, bld1[key])
        print(key,  bld2[key])
print("end of search")