def load_document(file_path):
    dic = {}
    with open(file_path, mode="r", encoding="utf-8") as f:
        for line in f:
            _id, rest = line.split(sep="\t", maxsplit=1)
            dic.update({int(_id): rest.strip()})
    return dic


def build_inverted_index(articles):
    new_dict = {}
    for key, value in articles.items():
        for item in value.split():
            new_dict.setdefault(item, []).append(key)

    new_dict2 = {k: set(v) for k, v in new_dict.items()}
    return new_dict2
